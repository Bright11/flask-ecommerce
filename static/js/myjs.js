
const categorysidebar=document.querySelector(".category-items")

function sidebarclick(){
    categorysidebar.classList.toggle('category-items-opend')
}


// searchbardiv
const search=document.querySelector(".searchbardiv")
const closeformbtn=document.querySelector(".closeform-div")

function opensearchform(){
    search.classList.toggle("searchitem")
    closeformbtn.classList.toggle("searchitem")
}


function closeform(){
    search.classList.remove("searchitem")
    closeformbtn.classList.remove("searchitem")
}

// nav

const openavmobile=document.querySelector(".topul")

function opennavemobilebtn(){
    openavmobile.classList.toggle("topulmobileopen")
}


// addcategory
const showtable=document.querySelector('.hidetable')

const myform=document.querySelector('.addcategoryfor-div')

function categoryform(){
    showtable.classList.toggle('showtable')
    namet=myform.classList.toggle('showform')
   if(namet){
    document.getElementById('showbtn').innerHTML='Show Table'
   }else{
    document.getElementById('showbtn').innerHTML='Show Category'
   }
}



