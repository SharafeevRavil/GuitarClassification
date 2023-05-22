//Импорты
const entities = require('@jetbrains/youtrack-scripting-api/entities');
const workflow = require('@jetbrains/youtrack-scripting-api/workflow');
//Экспорт правила для ютрека
exports.rule = entities.Issue.onChange({
  title: 'Rtm_system-use',
  guard: (ctx) => {
    return true;
  },
  action: (ctx) => {
    //Тело правила, которое запускается при
    const issue = ctx.issue;
    const fs = issue.fields;
    
    const oldValue = issue.oldValue("RTM_systemUse");
    const newValue = fs.RTM_systemUse;
    //Проверка на попытку ручного изменения поля RTM_systemUse - транзакция прерывается, если такая попытка была
    workflow.check(oldValue === newValue,
                   'Поле RTM_systemUse запрещено изменять! Оно системное!');
    
    console.log(issue.id);
    //Установка поля RTM_systemUse как краткое имя (id) тест-кейса
    fs.RTM_systemUse = issue.id;
  },
  requirements: {
  }
});
