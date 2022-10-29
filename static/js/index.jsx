// import {initializeApp } from "firebase/app";
// import { getDatabase, push, ref, set} from "firebase/database";
// import {getAnalytics} from "firebase/analytics";
//fd
// const firebaseConfig = {
//     apiKey: "AIzaSyBlJE9mBdjosSlAsvz9CY7EQWyd1EVnFSU",
//     authDomain: "vertible-d6c3f.firebaseapp.com",
//     databaseURL: "https://vertible-d6c3f-default-rtdb.firebaseio.com",
//     projectId: "vertible-d6c3f",
//     storageBucket: "vertible-d6c3f.appspot.com",
//     messagingSenderId: "1075957761941",
//     appId: "1:1075957761941:web:be18fa1201229c71cbd89c",
//     measurementId: "G-919RXPL769"
//   };
// const app = initializeApp(firebaseConfig);

// function writeUserData(userID, name, email) {
//     const db = getDatabase();
//     const reference = ref(db, 'users/' + userID);

//     set(reference, {
//         username: name,
//         email: email
//     });
// }

// writeUserData("hello", "fsdofisd", "ilikepie@gmail.com");



//Dropdown nav

const drop = document.querySelector("#dropdownNavbarLink");
const dropContent = document.querySelector("#dropdownNavbar");

console.log(drop);
console.log(dropContent);
drop.addEventListener("click", () => {
    dropContent.classList.toggle("hidden");
})


const insidedrop = document.querySelector("#insidedropdownNavbarLink");
const insidedropContent = document.querySelector("#insidedropdownNavbar");

console.log(insidedrop);
console.log(insidedropContent);
insidedrop.addEventListener("click", () => {
    insidedropContent.classList.toggle("hidden");
})

//mobile menu
const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");

btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
});

window.onresize = window.onload = function() {
    if(window.innerWidth > 766){
        menu.classList.add("hidden");
        insidedropContent.add("hidden");
    }
}

