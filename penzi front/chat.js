   // reading phone value
    function getphone() {
      return document.getElementById("msisdn").value;
    }

    // send request with body above
    async function postData(url = '', data = {}) {
      const myHeaders = new Headers();
      myHeaders.append('Content-Type', 'application/json');

      const response = await fetch(url, {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify(data)
      });

      const res = await response.json()

      return res
    }

    // counter - 0

    function start(e) {
      e.preventDefault()
      
      // create object phone, msg
      const start = {
        msg: 'penzi',
        msisdn: getphone(),
      };
      const register = {
        msg: 'start#mercy lemayan#30#female#Narok#Keiyan',
        msisdn:getphone(),
      }

      //switch counter 0-start, 1-details, 2-mg

      postData('http://127.0.0.1:5000/send',start).then(data=>{
        console.log(data)
        const node = document.createElement('div')
        node.innerHTML = data.reply
        document.getElementById("responses").appendChild(node)
        document.getElementById("sub").value='Send'
        // increent
      }).catch(error=>{
        console.log(error)
      })
    }

    


    // listen on submit
    // document.getElementById("myform").addEventListener("submit", myFunction);

    // prevent default
    document.getElementById("sub").addEventListener("click",start);
    
