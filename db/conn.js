// Mongodb Connection
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/Artow",{useCreateIndex:true,useNewUrlParser:true,useFindAndModify:false,useUnifiedTopology:true}).then(()=>{
    console.log("We Are Connected To DataBase")
}).catch((err)=>{
    console.log(err);
})