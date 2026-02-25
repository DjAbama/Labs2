function* counter() {
    let number = 0;
    while(true){
        yield number;
        number++;
    }
}


function iterator(generator, seconds) {

    const timer = setInterval(() => {
        console.log(generator.next().value);
    }, 500);

    setTimeout(() => {
        clearInterval(timer);
        }, seconds * 1000);
}



iterator(counter(), 5);

