const elementsToScrape = document.querySelectorAll("[tabindex='-1'] div");
const scrapedData = [];

elementsToScrape.forEach((element) => {
  const data = element.textContent.trim();
  scrapedData.push(data);
});

let dataString = scrapedData.join("\n");

const blob = new Blob([dataString], { type: "text/plain" });

const url = URL.createObjectURL(blob);

const link = document.createElement("a");
link.href = url;
link.download = "scraped_numbers.txt";
link.style.display = "none";

document.body.appendChild(link);

link.click();

document.body.removeChild(link);

URL.revokeObjectURL(url);
