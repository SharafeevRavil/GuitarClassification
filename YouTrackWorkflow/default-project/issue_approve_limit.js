//Импорты
const entities = require('@jetbrains/youtrack-scripting-api/entities');
const workflow = require('@jetbrains/youtrack-scripting-api/workflow');
//Экспорт правила для ютрека

exports.rule = entities.Issue.onChange({
  // TODO: give the rule a human-readable title
  title: 'Issue_approve_limit',
  guard: (ctx) => {
        return ctx.issue.fields.Stage;
  },
  action: (ctx) => {
    //Тело правила, которое запускается при изменении issue
    const issue = ctx.issue;
    const fs = issue.fields;
    
    const backlogName = "Backlog"
    const toDoName = "ToDo"
    const inProgressName = "InProgress";
    const incompleteName = "Incomplete";
    const reviewName = "Review";
    const testName = "Test";
    const doneName = "Done";
    
    const oldValue = issue.oldValue("Stage");
    const newValue = fs.Stage;
    console.log(oldValue, newValue)
    
    if(oldValue === null || oldValue.name === newValue.name)
      return;

    //Проверки для каждого перехода состояний
    var isDevLead = ctx.currentUser.hasRole('DevLead', ctx.issue.project);
    var isQa = ctx.currentUser.hasRole('QA', ctx.issue.project) || ctx.currentUser.hasRole('QALead', ctx.issue.project);
    workflow.check(oldValue.name != backlogName || newValue.name == toDoName,
                  `Нельзя перейти из ${oldValue.name} в ${newValue.name}`);
    workflow.check(oldValue.name != toDoName || newValue.name == inProgressName,
                   `Нельзя перейти из ${oldValue.name} в ${newValue.name}`);
    workflow.check(oldValue.name != inProgressName || newValue.name == incompleteName || newValue.name == reviewName,
                   `Нельзя перейти из ${oldValue.name} в ${newValue.name}`);
    workflow.check(oldValue.name != incompleteName || newValue.name == backlogName || newValue.name == inProgressName,
                   `Нельзя перейти из ${oldValue.name} в ${newValue.name}`);
    workflow.check(oldValue.name != reviewName || newValue.name == incompleteName || newValue.name == testName,
                   `Нельзя перейти из ${oldValue.name} в ${newValue.name}`);
    workflow.check(oldValue.name != testName || newValue.name == incompleteName || newValue.name == doneName,
                   `Нельзя перейти из ${oldValue.name} в ${newValue.name}`);
    workflow.check(oldValue.name != doneName || newValue.name == incompleteName,
                   `Нельзя перейти из ${oldValue.name} в ${newValue.name}`);
    workflow.check(oldValue.name != testName || newValue.name != doneName || (newValue.name == doneName && isQa),
                   'Только QA может тестировать задачи!');
    workflow.check(oldValue.name != reviewName || newValue.name != testName || (newValue.name == testName && isDevLead),
                   'Только DevLead может делать code review задачи!');
  },
  requirements: {
    // TODO: add requirements
  }
});
