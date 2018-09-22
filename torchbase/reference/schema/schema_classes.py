import json
import os.path
import decimal
import datetime
import six
from avrogen.dict_wrapper import DictWrapper
from avrogen import avrojson
from avro import schema as avro_schema
if six.PY3:    from avro.schema import SchemaFromJSONData as make_avsc_object
    
else:
    from avro.schema import make_avsc_object
    


def __read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()
from avro import protocol as avro_protocol

def __get_protocol(file_name):
    proto = avro_protocol.Parse(__read_file(file_name)) if six.PY3 else avro_protocol.parse(__read_file(file_name))
    return proto

PROTOCOL = __get_protocol(os.path.join(os.path.dirname(__file__), "protocol.avpr"))
__SCHEMAS = {}
def get_schema_type(fullname):
    return __SCHEMAS.get(fullname)
for rec in PROTOCOL.types:
    __SCHEMAS[rec.fullname] = rec
for resp in (six.itervalues(PROTOCOL.messages) if six.PY2 else PROTOCOL.messages):
    if isinstance(resp.response, (avro_schema.RecordSchema, avro_schema.EnumSchema)):
        __SCHEMAS[resp.response.fullname] = resp.response
PROTOCOL_MESSAGES = {m.name.lstrip("."):m for m in (six.itervalues(PROTOCOL.messages) if six.PY2 else PROTOCOL.messages)}



class SchemaClasses(object):
    
    
    pass
    class torchbase_models(object):
        
        class ProfileElementClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.ProfileElement")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.ProfileElementClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.LocusName = str()
                    self.AlleleName = str()
            
            
            @property
            def LocusName(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('LocusName')
            
            @LocusName.setter
            def LocusName(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['LocusName'] = value
            
            
            @property
            def AlleleName(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('AlleleName')
            
            @AlleleName.setter
            def AlleleName(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['AlleleName'] = value
            
            
        class VariantClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.Variant")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.VariantClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.Contig = str()
                    self.Position = int()
                    self.Ref = str()
                    self.Alt = str()
            
            
            @property
            def Contig(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Contig')
            
            @Contig.setter
            def Contig(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Contig'] = value
            
            
            @property
            def Position(self):
                """
                :rtype: int
                """
                return self._inner_dict.get('Position')
            
            @Position.setter
            def Position(self, value):
                #"""
                #:param int value:
                #"""
                self._inner_dict['Position'] = value
            
            
            @property
            def Ref(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Ref')
            
            @Ref.setter
            def Ref(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Ref'] = value
            
            
            @property
            def Alt(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Alt')
            
            @Alt.setter
            def Alt(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Alt'] = value
            
            
        class PresenceClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.Presence")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.PresenceClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.Name = str()
                    self.Presence = bool()
            
            
            @property
            def Name(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Name')
            
            @Name.setter
            def Name(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Name'] = value
            
            
            @property
            def Presence(self):
                """
                :rtype: bool
                """
                return self._inner_dict.get('Presence')
            
            @Presence.setter
            def Presence(self, value):
                #"""
                #:param bool value:
                #"""
                self._inner_dict['Presence'] = value
            
            
        class TypesClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.Types")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.TypesClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.Name = str()
                    self.profile = list()
                    self.variants = list()
                    self.presence = list()
            
            
            @property
            def Name(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Name')
            
            @Name.setter
            def Name(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Name'] = value
            
            
            @property
            def profile(self):
                """
                :rtype: list[SchemaClasses.torchbase_models.ProfileElementClass]
                """
                return self._inner_dict.get('profile')
            
            @profile.setter
            def profile(self, value):
                #"""
                #:param list[SchemaClasses.torchbase_models.ProfileElementClass] value:
                #"""
                self._inner_dict['profile'] = value
            
            
            @property
            def variants(self):
                """
                :rtype: list[SchemaClasses.torchbase_models.VariantClass]
                """
                return self._inner_dict.get('variants')
            
            @variants.setter
            def variants(self, value):
                #"""
                #:param list[SchemaClasses.torchbase_models.VariantClass] value:
                #"""
                self._inner_dict['variants'] = value
            
            
            @property
            def presence(self):
                """
                :rtype: list[SchemaClasses.torchbase_models.PresenceClass]
                """
                return self._inner_dict.get('presence')
            
            @presence.setter
            def presence(self, value):
                #"""
                #:param list[SchemaClasses.torchbase_models.PresenceClass] value:
                #"""
                self._inner_dict['presence'] = value
            
            
        class AlleleClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.Allele")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.AlleleClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.Name = str()
                    self.Hash = str()
            
            
            @property
            def Name(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Name')
            
            @Name.setter
            def Name(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Name'] = value
            
            
            @property
            def Hash(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Hash')
            
            @Hash.setter
            def Hash(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Hash'] = value
            
            
        class LocusClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.Locus")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.LocusClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.Name = str()
                    self.alleles = list()
            
            
            @property
            def Name(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Name')
            
            @Name.setter
            def Name(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Name'] = value
            
            
            @property
            def alleles(self):
                """
                :rtype: list[SchemaClasses.torchbase_models.AlleleClass]
                """
                return self._inner_dict.get('alleles')
            
            @alleles.setter
            def alleles(self, value):
                #"""
                #:param list[SchemaClasses.torchbase_models.AlleleClass] value:
                #"""
                self._inner_dict['alleles'] = value
            
            
        class ReferenceClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.Reference")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.ReferenceClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.loci = list()
            
            
            @property
            def loci(self):
                """
                :rtype: list[SchemaClasses.torchbase_models.LocusClass]
                """
                return self._inner_dict.get('loci')
            
            @loci.setter
            def loci(self, value):
                #"""
                #:param list[SchemaClasses.torchbase_models.LocusClass] value:
                #"""
                self._inner_dict['loci'] = value
            
            
        class QCClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.QC")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.QCClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.Coverage = None
                    self.VariantDepth = None
                    self.AverageDepth = None
                    self.ConsenusCutoff = None
                    self.Identity = None
                    self.MappingQuality = None
                    self.BaseQuality = None
                    self.VariantQuality = None
            
            
            @property
            def Coverage(self):
                """
                :rtype: float
                """
                return self._inner_dict.get('Coverage')
            
            @Coverage.setter
            def Coverage(self, value):
                #"""
                #:param float value:
                #"""
                self._inner_dict['Coverage'] = value
            
            
            @property
            def VariantDepth(self):
                """
                :rtype: int
                """
                return self._inner_dict.get('VariantDepth')
            
            @VariantDepth.setter
            def VariantDepth(self, value):
                #"""
                #:param int value:
                #"""
                self._inner_dict['VariantDepth'] = value
            
            
            @property
            def AverageDepth(self):
                """
                :rtype: float
                """
                return self._inner_dict.get('AverageDepth')
            
            @AverageDepth.setter
            def AverageDepth(self, value):
                #"""
                #:param float value:
                #"""
                self._inner_dict['AverageDepth'] = value
            
            
            @property
            def ConsenusCutoff(self):
                """
                :rtype: float
                """
                return self._inner_dict.get('ConsenusCutoff')
            
            @ConsenusCutoff.setter
            def ConsenusCutoff(self, value):
                #"""
                #:param float value:
                #"""
                self._inner_dict['ConsenusCutoff'] = value
            
            
            @property
            def Identity(self):
                """
                :rtype: float
                """
                return self._inner_dict.get('Identity')
            
            @Identity.setter
            def Identity(self, value):
                #"""
                #:param float value:
                #"""
                self._inner_dict['Identity'] = value
            
            
            @property
            def MappingQuality(self):
                """
                :rtype: int
                """
                return self._inner_dict.get('MappingQuality')
            
            @MappingQuality.setter
            def MappingQuality(self, value):
                #"""
                #:param int value:
                #"""
                self._inner_dict['MappingQuality'] = value
            
            
            @property
            def BaseQuality(self):
                """
                :rtype: int
                """
                return self._inner_dict.get('BaseQuality')
            
            @BaseQuality.setter
            def BaseQuality(self, value):
                #"""
                #:param int value:
                #"""
                self._inner_dict['BaseQuality'] = value
            
            
            @property
            def VariantQuality(self):
                """
                :rtype: int
                """
                return self._inner_dict.get('VariantQuality')
            
            @VariantQuality.setter
            def VariantQuality(self, value):
                #"""
                #:param int value:
                #"""
                self._inner_dict['VariantQuality'] = value
            
            
        class TorchModelClass(DictWrapper):
            
            """
            
            """
            
            
            RECORD_SCHEMA = get_schema_type("torchbase_models.TorchModel")
            
            
            def __init__(self, inner_dict=None):
                super(SchemaClasses.torchbase_models.TorchModelClass, self).__init__(inner_dict)
                if inner_dict is None:
                    self.Name = str()
                    self.Version = str()
                    self.Description = str()
                    self.reference = SchemaClasses.torchbase_models.ReferenceClass()
                    self.qc = SchemaClasses.torchbase_models.QCClass()
                    self.types = list()
            
            
            @property
            def Name(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Name')
            
            @Name.setter
            def Name(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Name'] = value
            
            
            @property
            def Version(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Version')
            
            @Version.setter
            def Version(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Version'] = value
            
            
            @property
            def Description(self):
                """
                :rtype: str
                """
                return self._inner_dict.get('Description')
            
            @Description.setter
            def Description(self, value):
                #"""
                #:param str value:
                #"""
                self._inner_dict['Description'] = value
            
            
            @property
            def reference(self):
                """
                :rtype: SchemaClasses.torchbase_models.ReferenceClass
                """
                return self._inner_dict.get('reference')
            
            @reference.setter
            def reference(self, value):
                #"""
                #:param SchemaClasses.torchbase_models.ReferenceClass value:
                #"""
                self._inner_dict['reference'] = value
            
            
            @property
            def qc(self):
                """
                :rtype: SchemaClasses.torchbase_models.QCClass
                """
                return self._inner_dict.get('qc')
            
            @qc.setter
            def qc(self, value):
                #"""
                #:param SchemaClasses.torchbase_models.QCClass value:
                #"""
                self._inner_dict['qc'] = value
            
            
            @property
            def types(self):
                """
                :rtype: list[SchemaClasses.torchbase_models.TypesClass]
                """
                return self._inner_dict.get('types')
            
            @types.setter
            def types(self, value):
                #"""
                #:param list[SchemaClasses.torchbase_models.TypesClass] value:
                #"""
                self._inner_dict['types'] = value
            
            
        
        pass


class RequestClasses(object):
    
    
    
    pass
__SCHEMA_TYPES = {
'torchbase_models.ProfileElement': SchemaClasses.torchbase_models.ProfileElementClass,
    'torchbase_models.Variant': SchemaClasses.torchbase_models.VariantClass,
    'torchbase_models.Presence': SchemaClasses.torchbase_models.PresenceClass,
    'torchbase_models.Types': SchemaClasses.torchbase_models.TypesClass,
    'torchbase_models.Allele': SchemaClasses.torchbase_models.AlleleClass,
    'torchbase_models.Locus': SchemaClasses.torchbase_models.LocusClass,
    'torchbase_models.Reference': SchemaClasses.torchbase_models.ReferenceClass,
    'torchbase_models.QC': SchemaClasses.torchbase_models.QCClass,
    'torchbase_models.TorchModel': SchemaClasses.torchbase_models.TorchModelClass,
    
}
_json_converter = avrojson.AvroJsonConverter(use_logical_types=False, schema_types=__SCHEMA_TYPES)

