function* clounter() {
    let number = 0;
    while(true){
        yield number;
        number++;
    }
}

let counter = clounter();
console.log(counter.next().value);
console.log(counter.next().value);
console.log(counter.next().value);