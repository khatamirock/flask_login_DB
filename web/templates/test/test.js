

const noteCard = document.querySelectorAll('.notes-card');
const popcard = document.querySelector('.doc');
const noteParent = document.querySelector('.card-container');
const closeBtn = document.querySelector('.close');



// noteParent.addEventListener('click', function (e) {
//     const target = e.target.closest('.notes-card');
//     if (!target) {
//         popcard.classList.add('hide');
//         return;
//     }
//     // console.log(target.innderHTML);
//     const text = target.querySelector('.note-body b').innerHTML;
//     popcard.querySelector('b').innerHTML = text;
//     popcard.classList.toggle('hide');


// });

// closeBtn.addEventListener('click', function () {
//     popcard.classList.add('hide');
// });



gsap.to('.cursor', {
    opacity: 0,
    duration: 0.76,
    ease: 'power3.in',
    repeat: -1,
})



let tl = gsap.timeline();

tl.from('.code', {

    duration: 1,
    y: 100,
    ease: 'power3.out',

})


    ;
