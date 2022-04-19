eel.expose(ErrorUpdater);
function ErrorUpdater(Error){
    document.getElementById("ErrorMessage").innerHTML = Error;
}

eel.expose(JoinServerButtonOnClick);
function JoinServerButtonOnClick(){
    var IP = document.getElementById("IP").value;
    var Port = document.getElementById("Port").value;
    var logs = document.getElementById("LogsBoxInput");
    if (logs.checked == true){
        logs = "True";
    }else{
        logs = "False";
    }
    var encrypt = document.getElementById("EncryptionBoxInput");
    if (encrypt.checked == true){
        encrypt = "True";
    }else{
        encrypt = "False";
    }
    var anom = document.getElementById("AnonymousUsernameInput");
    if (anom.checked == true){
        anom = "True";
    }else{
        anom = "False";
    }
    console.log(IP, Port, logs, encrypt, anom);
    eel.GetInputFromServerJoin(IP, Port, logs, encrypt, anom);
    window.location.href = "clientSide.html";
}

eel.expose(JoinServerButtonOnClick);
function CreateServerButtonOnClick(){
    var IP = document.getElementById("IP").value;
    var Port = document.getElementById("Port").value;
    var logs = document.getElementById("LogsBoxInput");
    if (logs.checked == true){
        logs = "True";
    }else{
        logs = "False";
    }
    var encrypt = document.getElementById("EncryptionBoxInput");
    if (encrypt.checked == true){
        encrypt = "True";
    }else{
        encrypt = "False";
    }
    var anom = document.getElementById("AnonymousUsernameInput");
    if (anom.checked == true){
        anom = "True";
    }else{
        anom = "False";
    }
    console.log(IP, Port, logs, encrypt, anom);
    eel.GetInputFromServerCreate(IP, Port, logs, encrypt, anom);
    window.location.href = "ServerDashboard.html";
}


eel.expose(ChangePage);
function ChangePage(NextPage){
    window.location.href = NextPage;
}

eel.expose(ForgotPasswordChangeNewPassword);
function ForgotPasswordChangeNewPassword(newPass){
    document.getElementById("ForgotPasswordPasswordOutput").value = newPass;
}

eel.expose(updateServerMessages);
function updateServerMessages(message){
    var old = document.getElementById("ServerMessages").value;
    document.getElementById("ServerMessages").value =  old + " " + message + "\n";
    document.getElementById("ServerMessages").scrollTop = document.getElementById("ServerMessages").scrollHeight;
}

eel.expose(updateUserMessages);
function updateUserMessages(message){
    var old = document.getElementById("UserMessages").value;
    document.getElementById("UserMessages").value =  old + " " + message + "\n";
    document.getElementById("UserMessages").scrollTop = document.getElementById("UserMessages").scrollHeight;
}

function SendMessage(){
    eel.clientSend(document.getElementById("MessageInput").value);
}

function CloseServer(){
    eel.CloseSocket();
}

function CloseUser(){
    eel.CloseUser();
}

function AccountCreationInputFieldCollection(){
    // var x = document.getElementById("AccountCreationUsername").value;
    // var y = document.getElementById("AccountCreationPassword1").value;
    // var z = document.getElementById("AccountCreationPassword2").value;
    eel.SignUp(document.getElementById("AccountCreationUsername").value,document.getElementById("AccountCreationPassword1").value,document.getElementById("AccountCreationPassword2").value);
}

function SigninInputFieldCollection(){
    var x = document.getElementById("SigninUsername").value;
    var y = document.getElementById("Signinpassword").value;
    eel.Login(x,y);
}

function AccountCreationButtonOnClick(){
    AccountCreationInputFieldCollection();
}

function SigninButtonOnClick(){
    SigninInputFieldCollection();
}

function ForgotPasswordOnClick(){
    eel.Forgot(document.getElementById("ForgotPasswordUsername").value);
}

eel.expose(GetUsername);
function GetUsername(username){
    sessionStorage.setItem("USERNAME", username);
}

eel.expose(ReturnUsername)
function ReturnUsername(){
    eel.clientSend(sessionStorage.getItem("USERNAME"));
}

function SetUsername(){
    document.getElementById("UserWelcome").value = "Signed In As, " + sessionStorage.getItem("USERNAME");
    document.getElementById("AnonymousUsernameInput").checked = true;
    }

eel.expose(GetIp);
function GetIp(IP){
    sessionStorage.setItem("LOCALIP", IP);
}

function SetIp(){
    document.getElementById("IP").value = sessionStorage.getItem("LOCALIP");
    document.getElementById("Port").value = 25565;
}

