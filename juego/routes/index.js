var express = require('express');
var router = express.Router();
var mysql = require('mysql');
var connection = mysql.createConnection({
	host : 'localhost',
	user : 'root',
	password : '',
	database : 'juegobd'
});
connection.connect();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});
var sesiones=Array();
router.get("/errorsession/",function(req,res){
	console.log("ERROR SESSION")
	res.writeHead("302",{"Location":"http://localhost:8000/ingresar/"});
	res.end();
});
router.get("/django/:id?",function(req,res){
	s.getSession(req.params.id,function(s){
		if(s.estado=="conectado")
		{
			req.params.username=s.name;
			sesiones[req.cookies.sessionid]={id:req.params.id,name:s.name};
			console.log(sesiones);
			res.render('index', { title: 'Express',sessionid:req.params.id});
		}else{
			res.writeHead("302",{"Location":"http://localhost:8000/ingresar/"});
			res.end();
		}
	});
	
});

router.get('/registrate/', function(req, res) {
  if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://localhost:8000/registrar/"});
		res.end();
		return;
	}
  res.render('registrate', { title: 'Express' });
});
router.get("/Login/",function(req,res){
	if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://localhost:8000/ingresar/"});
		res.end();
		return;
	}
	res.render("login",{})
})
router.get("/partidanueva",function(req,res){
	connection.query('select * from juego',function(err, docs) {
			res.render('ver', {partidas: docs});
	});		
});
router.get("/nuevapartida",function(req,res){
	res.render("partidanueva",{});
})
router.post("/nuevapartida",function(req,res){

	var	titulo=req.body.titulo;
		tipo=req.body.tipo;
		pregunta=req.body.pregunta;
		tiempo=req.body.tiempo;
		arte=req.body.arte;
		lenguaje=req.body.lenguaje;
		matematicas=req.body.matematicas;
		peliculas=req.body.peliculas;
		tecnologia=req.body.tecnologia;
		musica=req.body.musica;
	connection.query('INSERT INTO juego ( titulo, tipo, pregunta, tiempo, arte, lenguaje, matematicas, peliculas, tecnologia, musica ) VALUES(? ,? ,? ,? ,? ,? ,? ,? ,? ,? );',[ titulo, tipo, pregunta, tiempo, arte, lenguaje, matematicas, peliculas, tecnologia, musica], function(err, docs){
	if(err) res.json(err);
	res.redirect('/salaespera');	
	});
});
router.get("/salaespera",function(req,res){
	res.render("salaespera",{title:req.params.partida})
})

router.get("/chat/",function(req,res){
	res.render("chat",{});
})
router.get("/saladechat",function(req,res){
	res.render("saladechat",{title:"Sala"})
})

module.exports = router;
