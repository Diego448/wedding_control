function updateCountdown() {
    let daysElem = document.getElementById("countdownDays");
    let hoursElem = document.getElementById("countdownHours");
    let minutesElem = document.getElementById("countdownMinutes");

    let currentDate = new Date();
    let weddingDate = new Date("06/01/2024");
    let timeDiff = Math.abs(currentDate - weddingDate);
    let totalDiff = Math.ceil(timeDiff / (1000 * 60));
    let daysDiff = Math.floor((totalDiff / (24 * 60)));
    let hourDiff = Math.floor((totalDiff / 60) - (daysDiff * 24));
    let minuteDiff = (totalDiff) - (daysDiff * 60 * 24) - (hourDiff * 60);
    
    minutesElem.value = minuteDiff;
    hoursElem.value = hourDiff;
    daysElem.value = daysDiff;
    console.log(totalDiff);
}

function callCountdown() {
    setInterval(updateCountdown, 60000);
}

document.addEventListener('DOMContentLoaded', function() {
    updateCountdown();
    callCountdown();
});