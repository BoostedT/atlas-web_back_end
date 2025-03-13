export default function updateUniqItems(groceriesMap) {
  if (!(groceriesMap instanceof Map)) {
    throw new Error("Cannot process");
}

for (const [key, value] of groceriesMap) {
  if (value === 0) {
    groceriesMap.set(key, 100);
  }
}

return groceriesMap;
}
