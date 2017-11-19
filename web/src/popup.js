$(document).ready(function () {
  // TESTING PURPOSE
  // const memeUrl = 'https://api.imgflip.com/get_memes'
  // function getMemes() {
  //   return new Promise(function (resolve, reject) {
  //     fetch(memeUrl)
  //       .then(response => response.json())
  //       .then(data => { console.log(data); resolve(data) })
  //   })
  // }

  // (function getUrl(callback) {
  //   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  //     url = tabs[0].url;
  //     callback(url)
  //   });
  // })(console.log)

  var $divParent = $('<div>')
  $divParent.addClass('parent')
  $('html').removeClass('no-js')

  // WIP for additional tab  
  // $('#show-universal').on('click', function () {
  //   $('#facebook-feed').show()
  //   $('#universal-feed').hide()
  // })

  // $('#show-fb').on('click', function () {
  //   $('#facebook-feed').hide()
  //   $('#universal-feed').show()
  // })

  $('#search').on('change', function (e) {
    $('.divChild').remove();
    searchWord = document.getElementsByName('search')[0].value.toLowerCase();
    if (searchWord in dummyData) {
      dummyData[searchWord].forEach(function (meme) {
        $divChild = $('<div>')
        $divChild.addClass('divChild')
        $p = $('<p>')
        var text = meme.text
        var imageUrl = meme.memeImage
        var fbLink = meme.url
        $p.text(text)
        var $img = $('<img>')
        $img.attr({ name: text, src: imageUrl, width: 200, height: 200, href: fbLink })
        $img.click(function () {
          chrome.tabs.create({ url: $(this).attr('href') })
        })
        var $imgWrap = $('<div>')
        $imgWrap.addClass('imageWrapper')
        $divChild.append($p)
        $imgWrap.append($img)
        $divChild.append($imgWrap)
        $divParent.append($divChild)
        $('#memes').append($divParent)
      })
    }
  })
})



