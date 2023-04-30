// create a sleep function
// usage: sleep(ms).then(() => { /* do something */ });
const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}