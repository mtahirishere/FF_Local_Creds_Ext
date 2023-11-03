function extractDomain(url) {
    url = url.replace(/(https?:\/\/)?(www\.)?/i, '');
    const parts = url.split('/');
    const domain = parts[0];
    return domain;
}

function autofillCredentials() {
    const domain = window.location.href;
	
	console.log(window.location.href);
	//const data = {"domain": domain};
   // console.log(data);
// Define the URL to which you want to send the POST request
const url = 'http://192.168.0.177:8000/get-password';

// Create Data to be used ads POST body.
const data = {
  domain: domain,
};

// Send the POST request using fetch
fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
})
  .then((response) => response.json())
  .then((data) => {console.log("Success:", data)
  // get Username Feild Use 
  const usernameField2 = document.getElementById("userID")||document.getElementById("userID2");
  if (usernameField2)
  {
    const passwordField = document.getElementById("userPassword");

           if (usernameField2) {
               usernameField2.value = data.userName;
           }
           if (passwordField) {
               passwordField.value = data.password;
           }
  }
}
  )
  .catch((error) => console.error("Error:", error));
}
autofillCredentials();
