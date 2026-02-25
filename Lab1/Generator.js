function* counter() {
    let number = 0;
    while(true){
        yield number;
        number++;
    }
}


function iterator(generator, seconds) {
    counter = generator;
    time = seconds * 1000;

    const timer = setInterval(() => {
        console.log(counter.next().value);
    }, 500);

    setTimeout(() => {
        clearInterval(timer);
        }, time);
}



iterator(counter(), 5);

