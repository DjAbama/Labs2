function* counter() {
    let number = 0;
    while(true){
        yield number;
        number++;
    }
}





function iterator(generator, seconds) {
    this.generator = generator;
    time = seconds * 1000;

    const intervalId = setInterval(() => {
        console.log(this.generator.next().value);
        }, 500);

    setTimeout(() => {
        clearInterval(intervalId);
        }, 5000);
}



iterator(counter(), 5);

