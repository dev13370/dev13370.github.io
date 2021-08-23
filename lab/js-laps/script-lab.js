const BLACKLISTED_KEY_CODES = [38];
const COMMANDS = {
  help:
    'List of commands Supported: <span class="code">about</span>, <span class="code">ls</span>, <span class="code">location</span>, <span class="code">contact</span>',
    مساعدة:'قائمة الأوامر المدعومة: <span class="code">about</span>, <span class="code">ls</span>, <span class="code">location</span>, <span class="code">contact</span>',
  ls:
    'List of chall : <br><br> ~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall1.php"target="_blank">Chall 1 | URL </a><br> ~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall2.php"target="_blank">Chall 2 | comment </a><br>~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall3.php"target="_blank">Chall 3 | Stored Xss </a><br>~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall4.php"target="_blank">Chall 4 | Xss Login Page </a><br>~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall5.php"target="_blank">Chall 5 | Base64 Encoding </a><br>~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall6.php"target="_blank">Chall 6 | Removes Alert </a><br>~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall7.php"target="_blank">Chall 7 | Removes Script </a><br>~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall8.php"target="_blank">Chall 8 | preg_replace </a><br>~ <a href="https://labs-naplon.000webhostapp.com/labs-xss/chall9.php"target="_blank">Chall 9 | HTML Entities </a><br>',
  about:
    'Xss Labs | HackerNap<br>البرمجة عبر المواقع / هجوم حقن الشيفرة المصدريّة عبر موقع وسيط  هي أحد أنواع الهجوم التي يتعرض لها الأنظمة الحاسوبية، ونجدها خصوصاً في تطبيقات الإنترنت عبر ما يسمى برمجة بالحقن، التي يلجأ فيها بعض مستخدمي الإنترنت المخربين لإدخال بعض الجمل البرمجية للصفحات التي يستعرضها الآخرون. وعادة ما نجد هذا النوع من الهجوم في المواقع التي تستستخدم لغة اتش تي ام ال, <br>تم إنشاء هذا الموقع من أجل الممارسة ، من فضلك لا تخترق',

  location: 
    "Go to our official website:<br><a href='index.html' class='success link'>HackerNap</a>",
  contact:
    "You can contact me via the following links:<br><a href='http://www.snapchat.com/add/ii42' class='success link'>Snapchat</a> ,<a href='https://twitter.com/_naplon' class='success link'>Twitter</a>",
 
};
let userInput, terminalOutput;

const app = () => {
  userInput = document.getElementById("userInput");
  terminalOutput = document.getElementById("terminalOutput");
  document.getElementById("dummyKeyboard").focus();
  console.log("Application loaded");
};

const execute = function executeCommand(input) {
  let output;
  input = input.toLowerCase();
  if (input.length === 0) {
    return;
  }
  output = `<div class="terminal-line"><span class="success">➜</span> <span class="directory">~</span> ${input}</div>`;
  if (!COMMANDS.hasOwnProperty(input)) {
    output += `<div class="terminal-line">no such command: ${input}</div>`;
    console.log("Oops! no such command");
  } else {
    output += COMMANDS[input];
  }

  terminalOutput.innerHTML = `${
    terminalOutput.innerHTML
  }<div class="terminal-line">${output}</div>`;
  terminalOutput.scrollTop = terminalOutput.scrollHeight;
};

const key = function keyEvent(e) {
  const input = userInput.innerHTML;

  if (BLACKLISTED_KEY_CODES.includes(e.keyCode)) {
    return;
  }

  if (e.key === "Enter") {
    execute(input);
    userInput.innerHTML = "";
    return;
  }

  userInput.innerHTML = input + e.key;
};

const backspace = function backSpaceKeyEvent(e) {
  if (e.keyCode !== 8 && e.keyCode !== 46) {
    return;
  }
  userInput.innerHTML = userInput.innerHTML.slice(
    0,
    userInput.innerHTML.length - 1
  );
};

document.addEventListener("keydown", backspace);
document.addEventListener("keypress", key);
document.addEventListener("DOMContentLoaded", app);
