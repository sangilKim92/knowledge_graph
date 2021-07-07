const client = require('../elastic')

```
elasticsearch를 검색엔진으로 활용.
나온 결과들에 대해서 noej4를 이용해 순서매김 진행.
```

const es = (parent, args, context) =>{
    return new Promise((resolve, reject)=>{
        try
        {
            const rs = await client.
            console.log(rs)
            resolve(rs)
        }
        catch(err)
        {
            reject(err)
        }
    })
}


module.exports = {
    es:es
}