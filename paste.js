;(async () => {
  const scrollContainer = document.querySelector('.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x6ikm8r.x1odjw0f.x1hc1fzr')
  const scrapedData = []
  const fileName = Date.now().toString()

  do {
    const elementsToScrape = document.querySelectorAll('._ao3e')
    elementsToScrape.forEach((element) => {
      const data = element.textContent.trim()
      if (data.startsWith('+55')) { // change for your DDI
        scrapedData.push(data)
      }
    })
    scrollContainer.scrollBy(0, scrollContainer.clientHeight)
    await new Promise((resolve) => setTimeout(resolve, 1000))
  } while (
    scrollContainer.scrollTop + scrollContainer.clientHeight <
    scrollContainer.scrollHeight
  )

  let dataString = scrapedData
    .filter((data, index, datum) => datum.indexOf(data) === index)
    .join('\n')

  const blob = new Blob([dataString], { type: 'text/plain' })

  const url = URL.createObjectURL(blob)

  const link = document.createElement('a')
  link.href = url
  link.download = `${fileName}.txt`
  link.style.display = 'none'

  document.body.appendChild(link)

  link.click()

  document.body.removeChild(link)

  URL.revokeObjectURL(url)
})()
