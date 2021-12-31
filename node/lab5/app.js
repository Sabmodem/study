const readln = require('readline-sync');
const base = require('./base.json');
const express = require("express");

const app = express();
app.get("/", (req, res) => {
  res.send("<h2>Привет Express!</h2>");
});

app.get("/findRoot", (req, res) => {
  res.json(findRoot(base)[0]);
});

app.get("/findNodeById", (req, res) => {
  res.json(findNodeById(req.id)[0]);
});

const findRoot = () => base.filter(obj => obj.parent_id == null);
const findNodeById = (id) => base.filter(obj => obj.id == id);

const ask = (node) => {
  if(!node.question) {
    print_end(node);
    return;
  };
  console.log(node.question);
  for(let i in node.answers) {
    console.log([Number(i)],'\t',node.answers[i]);
  };
  const answer = readln.questionInt("Your choice? ");
  ask(findNodeById(node.next_nodes[answer])[0]);
};

const print_end = (node) => {
  console.log('Выбор сделан =>');
  console.log('=>\t', node.result);
  console.log(node.description);
};

// ask(findRoot(base)[0]);
app.listen(3000);
