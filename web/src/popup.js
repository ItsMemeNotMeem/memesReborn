$(document).ready(function () {
  const memeUrl = 'https://api.imgflip.com/get_memes'
  function getMemes() {
    return new Promise(function (resolve, reject) {
      fetch(memeUrl)
        .then(response => response.json())
        .then(data => { console.log(data); resolve(data) })
    })
  }

  (function getUrl(callback) {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      url = tabs[0].url;
      callback(url)
    });
  })(console.log)

  console.log('memes')


  var $divParent = $('<div>')
  $divParent.addClass('parent')
  
  // getMemes().then(function (data) {
  //   console.log('data', data)
  //   var memes = data.data.memes
  //   for (var i = 0; i < 12; i++) {
  //     $divChild = $('<div>')
  //     $p = $('<p>')
  //     memes[i]
  //     var name = memes[i].name
  //     var url = memes[i].url
  //     var width = memes[i].width
  //     var height = memes[i].height
  //     console.log('name url width height', name, url, width, height)
  //     $p.text(name)
  //     var $img = $('<img>')
  //     $img.attr({ name: name, src: url, width: 220, href: url })
  //     $img.click(function () {
  //       chrome.tabs.create({ url: $(this).attr('href') })
  //     })
  //     var $imgWrap = $('<div>')
  //     $imgWrap.addClass('imageWrapper')
  //     $divChild.append($p)
  //     $imgWrap.append($img)
  //     $divChild.append($imgWrap)
  //     $divParent.append($divChild)
  //   }
  //   $('#memes').append($divParent)
  // })

  $('#show-universal').on('click',function(){
    $('#facebook-feed').show()
    $('#universal-feed').hide()
  })
  $('#show-fb').on('click', function(){
    $('#facebook-feed').hide()
    $('#universal-feed').show()
  })
  $('#search').on('change', function (e) {
    $('.divChild').remove();
    searchWord = document.getElementsByName('search')[0].value.toLowerCase();    
    getMemes().then(function (data) {

      var memes = data.data.memes;
      for (let i = 0; i < memes.length; i++) {
        if (memes[i].name.toLowerCase().includes(searchWord)) {
          $divChild = $('<div>')
          $divChild.addClass('divChild')
          $p = $('<p>')
          memes[i]
          var name = memes[i].name
          var url = memes[i].url
          var width = memes[i].width
          var height = memes[i].height
          console.log('name url width height', name, url, width, height)
          $p.text(name)
          var $img = $('<img>')
          $img.attr({ name: name, src: url, width: 200, href: url })
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
        }


      }

    })
  })

})



