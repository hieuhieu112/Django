const searchBar = document.querySelector(".search input"),
const spanBar = document.querySelector(".search span"),
searchIcon = document.querySelector(".search button"),
usersList = document.querySelector(".users-list");

spanBar.onclick = ()=>{
  console.log(1)
  searchBar.classList.toggle("show");
  searchIcon.classList.toggle("active");
  searchBar.focus();
  if(searchBar.classList.contains("active")){
    searchBar.value = "";
    searchBar.classList.remove("active");
  }
}

searchBar.onkeyup = ()=>{
 console.log(1)
  let searchTerm = searchBar.value;
  if(searchTerm != ""){
    searchBar.classList.add("active");
  }else{
    searchBar.classList.remove("active");
  }

}


