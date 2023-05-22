//Импорты
const entities = require('@jetbrains/youtrack-scripting-api/entities');
//Экспорт правила для ютрека
exports.rule = entities.Issue.action({
  title: 'Create-execution',
  userInput: null,
  command: 'create-execution',
  guard: (ctx) => {
    const isTestPlan = ctx.issue.fields.Тип.name === "Test Plan";
    return isTestPlan;
  },
  action: (ctx) => {
    //Тело правила, которое запускается при изменении issue
    
    //Функция GUID
    function broofa() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
            return v.toString(16);
        });
    }

    const issue = ctx.issue;
    
    console.log('execute');
    console.log(ctx.Тип["Test Execution"]);
    
    const exGuid = broofa();
    //Создание запуска теста
    const testExecution = new entities.Issue(ctx.currentUser, issue.project,
                                             issue.summary + ` [Вызов ${exGuid}]`);
    testExecution.fields.Type = ctx.Тип["Test Execution"];
    testExecution.links['дублирует'].add(issue);
    //создание каждого вложенного тест-кейса
    issue.links['includes'].forEach(taskIssue => {
      console.log(taskIssue);
      const testCaseExec = new entities.Issue(ctx.currentUser, issue.project,
                                               taskIssue.summary + ` [Вызов ${exGuid}]`);
      testCaseExec.fields.Type = ctx.Тип["Test Case Execution"];
      testCaseExec.description = taskIssue.description;
      testCaseExec.links['дублирует'].add(taskIssue);
      testCaseExec.links['included in'].add(testExecution);
    });
  },
  requirements: {
    Тип: {
      type: entities.EnumField.fieldType,
      name: 'Тип',
      "Test Execution": { name: 'Test Execution' },
      "Test Case Execution": { name: 'Test Case Execution' }
  	},
  }
});
