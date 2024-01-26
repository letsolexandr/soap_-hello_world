
## run service
```bash
docker compose build
docker compose up
```

## get wsdl 
```bash
curl  http://0.0.0.0/trembita/soap/?wsdl
```
### call local server soap
 ```bash
curl --location --request POST 'http://0.0.0.0:8000/trembita/soap/' \
--header 'Content-Type: application/xml' \
--data-raw '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:trem="http://trembita.gov.ua">
   <soapenv:Header/>
   <soapenv:Body>
      <trem:getPersonInfoPy>
         <!--Optional:-->
         <trem:personId>6060606060</trem:personId>
      </trem:getPersonInfoPy>
   </soapenv:Body>
</soapenv:Envelope>'
```

## get REST 
```bash
curl  http://0.0.0.0/trembita/rest/
```
### call local server rest
```bash
curl --location --request GET 'http://0.0.0.0:8000/trembita/rest/person/1/'
```

