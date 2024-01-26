from lxml import etree
import re
import logging
from django.views.decorators.csrf import csrf_exempt
from spyne.server.django import DjangoApplication
from spyne.protocol.soap import Soap11
from spyne.model.complex import ComplexModel
from spyne import Application, rpc, ServiceBase, Integer, String, Date

from soapservice.models import Person

logging.basicConfig(level=logging.DEBUG)


class ServiceDateResult(ComplexModel):
    inn = String
    firstname = String
    surname = String
    birthdate = Date
    passport_ser = String
    passport_num = String


def to_dict(element):
    ret = {}
    if element.getchildren() == []:
        return element.text
    else:
        for elem in element.getchildren():
            subdict = to_dict(elem)
            ret[re.sub('{.*}', '', elem.tag)] = subdict
        return ret


class Soap(ServiceBase):
    @rpc(String, _returns=ServiceDateResult)
    def getPersonInfoPy(ctx, personId):
        print('-'*100)
        print("Request inn: " + personId)
        print(ctx.in_string)
        soapMsg = to_dict(ctx.in_document)
        try:
            print("UXP Heades information:")
            print("client.xRoadInstance = " +
                  soapMsg.get('Header').get('client').get('xRoadInstance'))
            print("client.memberClass = " +
                  soapMsg.get('Header').get('client').get('memberClass'))
            print("client.memberCode = " +
                  soapMsg.get('Header').get('client').get('memberCode'))
            print("client.subsystemCode = " +
                  soapMsg.get('Header').get('client').get('subsystemCode'))
            print("service.xRoadInstance = " +
                  soapMsg.get('Header').get('service').get('xRoadInstance'))
            print("service.memberClass = " +
                  soapMsg.get('Header').get('service').get('memberClass'))
            print("service.memberCode = " +
                  soapMsg.get('Header').get('service').get('memberCode'))
            print("service.subsystemCode = " +
                  soapMsg.get('Header').get('service').get('subsystemCode'))
            print("service.serviceCode = " +
                  soapMsg.get('Header').get('service').get('serviceCode'))
            print("id = " + soapMsg.get('Header').get('id'))
            print("userId = " + soapMsg.get('Header').get('userId', 'NONE'))
        except:
            print("Save result")
            person = Person.objects.get(inn=personId)
            res = ServiceDateResult(
                inn=person.inn,
                firstname=person.firstname,
                surname=person.surname,
                birthdate=person.birthdate,
                passport_ser=person.passport_ser,
                passport_num=person.passport_num
            )
            print('*'*100)
            return res


application = Application([Soap],
                          tns='http://trembita.gov.ua',
                          in_protocol=Soap11(validator='soft'),
                          out_protocol=Soap11()
                          )
hello_app = csrf_exempt(DjangoApplication(application))
