from .schema_classes import SchemaClasses as S
from .schema_classes import RequestClasses as R


ElementClass = S.torchbase_models.ProfileElementClass
Variant = S.torchbase_models.VariantClass
Presence = S.torchbase_models.PresenceClass
Types = S.torchbase_models.TypesClass
Allele = S.torchbase_models.AlleleClass
Locus = S.torchbase_models.LocusClass
Reference = S.torchbase_models.ReferenceClass
QC = S.torchbase_models.QCClass
Version = R.torchbase_models.VersionRequestClass
Description = R.torchbase_models.DescriptionRequestClass
Name = R.torchbase_models.NameRequestClass