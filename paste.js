const elementsToScrape = document.querySelectorAll("._2h0YP");
const scrapedData = [];
const fileName = Date.now().toString()

elementsToScrape.forEach((element) => {
  const data = element.textContent.trim();
  if(data.startsWith('+55')) // change for your DDI
  scrapedData.push(data);
});

let dataString = scrapedData.join("\n");

const blob = new Blob([dataString], { type: "text/plain" });

const url = URL.createObjectURL(blob);

const link = document.createElement("a");
link.href = url;
link.download = `${fileName}.txt`;
link.style.display = "none";

document.body.appendChild(link);

link.click();

document.body.removeChild(link);

URL.revokeObjectURL(url);
