const express = require("express");
const app = express();
const path = require("path");
const port = process.env.PORT || 8000;
require("../db/conn");
const hbs = require("hbs");
const chalk = require("chalk");
const Regester = require("../models/registration");
const bcrypt = require("bcryptjs");




// Path Of The Folders
const publicPath = path.join(__dirname,"../public");
const viewsPath = path.join(__dirname,"../templates/views");
const Partials_path = path.join(__dirname,"../templates/partials");

app.use(express.static(publicPath));

app.set("view engine","hbs");
app.set("views",viewsPath);
hbs.registerPartials(Partials_path);



// Need For Post Requests To Convert The Form to Json Format
app.use(express.json());
app.use(express.urlencoded({extended:false}));



app.get("/",(req,res)=>{
    res.render("signup");
});


app.post("/",async(req,res)=>{
    try {
    const UserData = new Regester({
        name : req.body.name,
        email : req.body.email,
        mobile : req.body.mobile,
        password : req.body.password,
        cpassword : req.body.cpassword
    });

    if(UserData.password === UserData.cpassword){
        const UserDataSaver = await UserData.save();
        console.log(UserDataSaver);
        res.status(201).render("redirection");
    }else{
        res.send("Passwords are not matching");
    }

    } catch (error) {
       res.status(400).send(error);
    }
});



app.get("/login",(req,res)=>{
    res.render("login");
});




app.get("/redirection",(req,res)=>{
    res.render("redirection");
})


app.get("/artistpackage",(req,res)=>{
    res.render("artistpackages")
});




app.post("/login",async(req,res)=>{
    try {
        const userEmail = req.body.email;
        const userPassword = req.body.password;
        const MatchingTheData = await Regester.findOne({email:userEmail});
     
        const isMatch = await bcrypt.compare(userPassword,MatchingTheData.password);

        if(isMatch){
            res.status(201).render("index");
        }else{
            res.send("Invalid Login Details");
        }

        } catch (error) {
        res.status(400).send("Invalid Login Details");
        }
});

app.get("/home",(req,res)=>{
    res.render("index");
});



app.listen(port,()=>{
    console.log(chalk.green.inverse(`Your Site Is Live In http://127.0.0.1:8000`));
});