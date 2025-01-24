// ageCalculator.js

// Function to calculate age
function calculateAge(birthYear) {
  const currentYear = new Date().getFullYear();
  const age = currentYear - birthYear;
  return age;
}

// Prompt user for birth year
console.log("Enter your birth year:");
const birthYear = parseInt(prompt());

// Calculate and display age
const age = calculateAge(birthYear);
console.log(`You are ${age} years old.`);