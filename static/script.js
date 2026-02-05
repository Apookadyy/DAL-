
const output = document.getElementById("output");

function loadTips(){
  fetch("/tips").then(r=>r.json()).then(data=>{
    output.innerHTML="";
    data.forEach(t=>output.innerHTML+=`<li>${t}</li>`);
  });
}

function takeQuiz(){
  fetch("/quiz",{
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({answer:"def"})
  }).then(r=>r.json()).then(d=>alert("Correct: "+d.correct));
}

function saveNote(){
  fetch("/notes",{
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({note:note.value})
  }).then(()=>alert("Saved"));
}
