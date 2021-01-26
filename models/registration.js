const express = require("express");
const mongoose = require("mongoose");
const validator = require("validator");
const bcrypt = require("bcryptjs");


const regestrationSchema = mongoose.Schema({
    name :{
        type : String,
        required : true,
        minLength : 3,
    },
    email : {
        type : String,
        required : true,
        lowercase : true,
        validate(value){
            if(!validator.isEmail(value)){
                throw new Error("Invalid Email");
            }
        }
    },
    mobile : {
        type : Number,
        required : true,
        minLength : 10,
    },
    password : {
        type : String,
        required : true,
    },
    cpassword : {
        type : String,
        required : true,
    }
});


// MiddleWare For Bcrypt Or Hashing The Passwords

regestrationSchema.pre("save",async function(next){
    if(this.isModified("password")){
        this.password = await bcrypt.hash(this.password,10);
    }
    next();
})




const Regester = mongoose.model("Regester",regestrationSchema);
module.exports = Regester;