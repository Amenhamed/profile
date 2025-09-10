window.addEventListener('scroll' , function(){
   let scrol =document.querySelectorAll('.scrol');
   scrol.forEach( element=>{
    let rect = element.getBoundingClientRect();
    if(rect.top<=this.window.innerHeight && rect.bottom>=0){
        element.classList.add('active');
    }else{
        element.classList.remove('active');
    }
   });
});
let texte = " Welcome to My Developer Portfolio i am AMEN allah hamed Building Full-Stack Web Solutions from Idea to Launch"
let tp =document.getElementById('tp')
let index =0
function typetexte() {
    if (index<texte.length ) {tp.textContent+=texte.charAt(index);
        index++;
        setTimeout(typetexte , 100); 
    }
}
typetexte();

