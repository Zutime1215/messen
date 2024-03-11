const express = require('express');
const fs = require('fs');
const server = express();

//bodyParser
server.use(express.json());
server.use(express.static('public'));


server.post('/',(req, res) =>{
  var id = Date.now();
  var old_msg = JSON.parse(fs.readFileSync('data.json', 'utf-8'));
  old_msg.push(
    {
      "name": req.body["name"],
      "id": (id - id%1000)/1000,
      "msg": req.body["msg"]
    }
  )
  fs.writeFileSync('data.json', JSON.stringify(old_msg));
  res.send("ok")
})

server.get('/', (req, res) => {
  res.json(JSON.parse(fs.readFileSync('data.json', 'utf-8')))
})


server.listen(8080, () => {
  console.log('server started');
});

