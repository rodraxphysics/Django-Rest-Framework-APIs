const contentContainer=document.getElementById("content-container")
const loginForm = document.getElementById("login-form")
const searchForm = document.getElementById("search-form");
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) { loginForm.addEventListener("submit", handleLogin) }

if (searchForm) {
  searchForm.addEventListener("submit", handleSearch);
}

function handleLogin(event){
    event.preventDefault()

    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    const options = { method: "POST", headers: { "Content-Type": "application/json" }, body: bodyStr }
    console.log (bodyStr)

    fetch(loginEndpoint, options)
        .then(response => {

            return response.json()
        })
        .then(authData => { handleAuthData (authData,getProductList)})
        .catch(err=> {console.log(err)})
}


function handleSearch(event) {
    event.preventDefault();

    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/search/?${searchParams}`;
    const headers = { "Content-Type": "application/json" };
    const authToken = localStorage.getItem("access")

    if (authToken) {
        headers["Authorization"] = `$Bearer ${authToken}`;
    }
    const options = { method: "GET", headers:headers };


    fetch(endpoint, options)
        .then((response) => {
        return response.json();
        })
        .then(data=>{writeToContainer(data)})
        .catch((err) => {
        console.log(err);
        });
    }


function handleAuthData(authData,callback) {
    localStorage.setItem("access", authData.access);
    localStorage.setItem("refresh", authData.refresh);
    if (callback){callback()}
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML="<pre>" +JSON.stringify(data,null,4)+"</pre>"

    }

}

function isTokenNotValid(jsonData){
  if (jsonData.code && jsonData.code === "token_not_valid") {
    alert("Please login again");
  }
}
function getProductList() {
    const endpoint = `${baseEndpoint}/products/`;
    const options = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem("access")}`,
      },
    };
    fetch(endpoint, options)
        .then(response => response.json())
        .then(data => {
            isTokenNotValid(data)
            writeToContainer(data)

        })
}
