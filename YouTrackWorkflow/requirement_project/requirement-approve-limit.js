//Импорты
const entities = require('@jetbrains/youtrack-scripting-api/entities');
const workflow = require('@jetbrains/youtrack-scripting-api/workflow');
//Экспорт правила для ютрека
exports.rule = entities.Issue.onChange({
  title: 'Requirement-approve-limit',
  guard: (ctx) => {
    return ctx.issue.fields.State;
    //return true;
  },
  action: (ctx) => {
    //Тело правила, которое запускается при изменении issue
    const issue = ctx.issue;
    const fs = issue.fields;
    
    const acceptedName = "Accepted";
    const notAcceptedName = "Not accepted";
    
    const oldValue = issue.oldValue("State");
    const newValue = fs.State;
    
    if(oldValue === null || oldValue.name === newValue.name)
      return;
    //Проверка на роль
    var hasRole = ctx.currentUser.hasRole('Key User', ctx.issue.project);
    workflow.check(hasRole,
                   'Только Key User может принимать требования!');
    //Запрет отката приемки требований
    const tryingToUnaccept = oldValue.name === acceptedName && newValue.name === notAcceptedName;
    workflow.check(!tryingToUnaccept,
                   'Требование было принято, невозможно перевести его в состояние "Не принято"!');
  },
  requirements: {
  }
});
