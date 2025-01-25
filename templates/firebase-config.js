// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBcRSZTGqSe6tP47sOYw7-GH-H8uvcwiHQ",
  authDomain: "innovateher25.firebaseapp.com",
  projectId: "innovateher25",
  storageBucket: "innovateher25.firebasestorage.app",
  messagingSenderId: "726795410942",
  appId: "1:726795410942:web:a948a64058eabdc70e74af",
  measurementId: "G-FZEEPZRJ78"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);