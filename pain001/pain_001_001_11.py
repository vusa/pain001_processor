from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11"


@dataclass
class AccountSchemeName1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class ActiveOrHistoricCurrencyAndAmount:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        }
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        }
    )


class AddressType2Code(Enum):
    ADDR = "ADDR"
    PBOX = "PBOX"
    HOME = "HOME"
    BIZZ = "BIZZ"
    MLTO = "MLTO"
    DLVY = "DLVY"


class AdviceType1Code(Enum):
    ADWD = "ADWD"
    ADND = "ADND"


class Authorisation1Code(Enum):
    AUTH = "AUTH"
    FDET = "FDET"
    FSUM = "FSUM"
    ILEV = "ILEV"


@dataclass
class CashAccountType2Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class CategoryPurpose1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class ChargeBearerType1Code(Enum):
    DEBT = "DEBT"
    CRED = "CRED"
    SHAR = "SHAR"
    SLEV = "SLEV"


class ChequeDelivery1Code(Enum):
    MLDB = "MLDB"
    MLCD = "MLCD"
    MLFA = "MLFA"
    CRDB = "CRDB"
    CRCD = "CRCD"
    CRFA = "CRFA"
    PUDB = "PUDB"
    PUCD = "PUCD"
    PUFA = "PUFA"
    RGDB = "RGDB"
    RGCD = "RGCD"
    RGFA = "RGFA"


class ChequeType2Code(Enum):
    CCHQ = "CCHQ"
    CCCH = "CCCH"
    BCHQ = "BCHQ"
    DRFT = "DRFT"
    ELDR = "ELDR"


@dataclass
class ClearingSystemIdentification2Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 5,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class CreditDebitCode(Enum):
    CRDT = "CRDT"
    DBIT = "DBIT"


@dataclass
class DateAndDateTime2Choice:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class DateAndPlaceOfBirth1:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        }
    )


@dataclass
class DatePeriod2:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )


@dataclass
class DiscountAmountType1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class DocumentLineType1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class DocumentType3Code(Enum):
    RADM = "RADM"
    RPIN = "RPIN"
    FXDR = "FXDR"
    DISP = "DISP"
    PUOR = "PUOR"
    SCOR = "SCOR"


class DocumentType6Code(Enum):
    MSIN = "MSIN"
    CNFA = "CNFA"
    DNFA = "DNFA"
    CINV = "CINV"
    CREN = "CREN"
    DEBN = "DEBN"
    HIRI = "HIRI"
    SBIN = "SBIN"
    CMCN = "CMCN"
    SOAC = "SOAC"
    DISP = "DISP"
    BOLD = "BOLD"
    VCHR = "VCHR"
    AROI = "AROI"
    TSUT = "TSUT"
    PUOR = "PUOR"


class ExchangeRateType1Code(Enum):
    SPOT = "SPOT"
    SALE = "SALE"
    AGRD = "AGRD"


@dataclass
class FinancialIdentificationSchemeName1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class Frequency6Code(Enum):
    YEAR = "YEAR"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    WEEK = "WEEK"
    DAIL = "DAIL"
    ADHO = "ADHO"
    INDA = "INDA"
    FRTN = "FRTN"


@dataclass
class GarnishmentType1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class GenericIdentification30:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class InstructionForCreditorAgent3:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )


@dataclass
class InstructionForDebtorAgent1:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )


@dataclass
class LocalInstrument2Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class MandateClassification1Code(Enum):
    FIXE = "FIXE"
    USGB = "USGB"
    VARI = "VARI"


@dataclass
class MandateSetupReason1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )


class NamePrefix2Code(Enum):
    DOCT = "DOCT"
    MADM = "MADM"
    MISS = "MISS"
    MIST = "MIST"
    MIKS = "MIKS"


@dataclass
class OrganisationIdentificationSchemeName1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class OtherContact1:
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class PaymentIdentification6:
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        }
    )


@dataclass
class PaymentInitiationSource1:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        }
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class PaymentMethod3Code(Enum):
    CHK = "CHK"
    TRF = "TRF"
    TRA = "TRA"


@dataclass
class PersonIdentificationSchemeName1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class PreferredContactMethod1Code(Enum):
    LETT = "LETT"
    MAIL = "MAIL"
    PHON = "PHON"
    FAXX = "FAXX"
    CELL = "CELL"


class Priority2Code(Enum):
    HIGH = "HIGH"
    NORM = "NORM"


@dataclass
class ProxyAccountType1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class Purpose2Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class RegulatoryAuthority2:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z]{2,2}",
        }
    )


class RegulatoryReportingType1Code(Enum):
    CRED = "CRED"
    DEBT = "DEBT"
    BOTH = "BOTH"


class RemittanceLocationMethod2Code(Enum):
    FAXI = "FAXI"
    EDIC = "EDIC"
    URID = "URID"
    EMAL = "EMAL"
    POST = "POST"
    SMSM = "SMSM"


@dataclass
class ServiceLevel8Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class SupplementaryDataEnvelope1:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class TaxAmountType1Choice:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class TaxAuthorisation1:
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )


@dataclass
class TaxParty1:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


class TaxRecordPeriod1Code(Enum):
    MM01 = "MM01"
    MM02 = "MM02"
    MM03 = "MM03"
    MM04 = "MM04"
    MM05 = "MM05"
    MM06 = "MM06"
    MM07 = "MM07"
    MM08 = "MM08"
    MM09 = "MM09"
    MM10 = "MM10"
    MM11 = "MM11"
    MM12 = "MM12"
    QTR1 = "QTR1"
    QTR2 = "QTR2"
    QTR3 = "QTR3"
    QTR4 = "QTR4"
    HLF1 = "HLF1"
    HLF2 = "HLF2"


@dataclass
class AddressType3Choice:
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prtry: Optional[GenericIdentification30] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class AdviceType1Choice:
    cd: Optional[AdviceType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class Authorisation1Choice:
    cd: Optional[Authorisation1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class ChequeDeliveryMethod1Choice:
    cd: Optional[ChequeDelivery1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class ClearingSystemMemberIdentification2:
    clr_sys_id: Optional[ClearingSystemIdentification2Choice] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class Contact4:
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        }
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        }
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        }
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 2048,
        }
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )
    othr: List[OtherContact1] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prefrd_mtd: Optional[PreferredContactMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class CreditorReferenceType1Choice:
    cd: Optional[DocumentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class DiscountAmountAndType1:
    tp: Optional[DiscountAmountType1Choice] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )


@dataclass
class DocumentAdjustment1:
    amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 4,
        }
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )


@dataclass
class DocumentLineType1:
    cd_or_prtry: Optional[DocumentLineType1Choice] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class EquivalentAmount2:
    amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    ccy_of_trf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOfTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        }
    )


@dataclass
class ExchangeRate1:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z]{3,3}",
        }
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        }
    )
    rate_tp: Optional[ExchangeRateType1Code] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ctrct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class FrequencyAndMoment1:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    pt_in_tm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "pattern": r"[0-9]{2}",
        }
    )


@dataclass
class FrequencyPeriod1:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    cnt_per_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CntPerPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        }
    )


@dataclass
class GarnishmentType1:
    cd_or_prtry: Optional[GarnishmentType1Choice] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class GenericAccountIdentification1:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        }
    )
    schme_nm: Optional[AccountSchemeName1Choice] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class GenericFinancialIdentification1:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1Choice] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class GenericOrganisationIdentification1:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1Choice] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class GenericPersonIdentification1:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: Optional[PersonIdentificationSchemeName1Choice] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class MandateClassification1Choice:
    cd: Optional[MandateClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class PaymentTypeInformation26:
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    svc_lvl: List[ServiceLevel8Choice] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    lcl_instrm: Optional[LocalInstrument2Choice] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ctgy_purp: Optional[CategoryPurpose1Choice] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class ProxyAccountIdentification1:
    tp: Optional[ProxyAccountType1Choice] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        }
    )


@dataclass
class ReferredDocumentType3Choice:
    cd: Optional[DocumentType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class StructuredRegulatoryReporting3:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z]{2,2}",
        }
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 10,
        }
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    inf: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class SupplementaryData1:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 350,
        }
    )
    envlp: Optional[SupplementaryDataEnvelope1] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )


@dataclass
class TaxAmountAndType1:
    tp: Optional[TaxAmountType1Choice] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )


@dataclass
class TaxParty2:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    authstn: Optional[TaxAuthorisation1] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class TaxPeriod3:
    yr: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Yr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    tp: Optional[TaxRecordPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    fr_to_dt: Optional[DatePeriod2] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class AccountIdentification4Choice:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        }
    )
    othr: Optional[GenericAccountIdentification1] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class AdviceType1:
    cdt_advc: Optional[AdviceType1Choice] = field(
        default=None,
        metadata={
            "name": "CdtAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dbt_advc: Optional[AdviceType1Choice] = field(
        default=None,
        metadata={
            "name": "DbtAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class AmountType4Choice:
    instd_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    eqvt_amt: Optional[EquivalentAmount2] = field(
        default=None,
        metadata={
            "name": "EqvtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class CreditorReferenceType2:
    cd_or_prtry: Optional[CreditorReferenceType1Choice] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class DocumentLineIdentification1:
    tp: Optional[DocumentLineType1] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class Frequency36Choice:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prd: Optional[FrequencyPeriod1] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    pt_in_tm: Optional[FrequencyAndMoment1] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class MandateTypeInformation2:
    svc_lvl: Optional[ServiceLevel8Choice] = field(
        default=None,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    lcl_instrm: Optional[LocalInstrument2Choice] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ctgy_purp: Optional[CategoryPurpose1Choice] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    clssfctn: Optional[MandateClassification1Choice] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class OrganisationIdentification29:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        }
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        }
    )
    othr: List[GenericOrganisationIdentification1] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class PersonIdentification13:
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    othr: List[GenericPersonIdentification1] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class PostalAddress24:
    adr_tp: Optional[AddressType3Choice] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 16,
        }
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 16,
        }
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 16,
        }
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z]{2,2}",
        }
    )
    adr_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        }
    )


@dataclass
class ReferredDocumentType4:
    cd_or_prtry: Optional[ReferredDocumentType3Choice] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class RegulatoryReporting3:
    dbt_cdt_rptg_ind: Optional[RegulatoryReportingType1Code] = field(
        default=None,
        metadata={
            "name": "DbtCdtRptgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    authrty: Optional[RegulatoryAuthority2] = field(
        default=None,
        metadata={
            "name": "Authrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dtls: List[StructuredRegulatoryReporting3] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class RemittanceAmount2:
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dscnt_apld_amt: List[DiscountAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    tax_amt: List[TaxAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    adjstmnt_amt_and_rsn: List[DocumentAdjustment1] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class RemittanceAmount3:
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dscnt_apld_amt: List[DiscountAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    tax_amt: List[TaxAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    adjstmnt_amt_and_rsn: List[DocumentAdjustment1] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class TaxRecordDetails3:
    prd: Optional[TaxPeriod3] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )


@dataclass
class BranchData3:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        }
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    pstl_adr: Optional[PostalAddress24] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class CashAccount40:
    id: Optional[AccountIdentification4Choice] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    tp: Optional[CashAccountType2Choice] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z]{3,3}",
        }
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 70,
        }
    )
    prxy: Optional[ProxyAccountIdentification1] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class CreditTransferMandateData1:
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    tp: Optional[MandateTypeInformation2] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dt_of_vrfctn: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtOfVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    elctrnc_sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ElctrncSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        }
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    fnl_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    frqcy: Optional[Frequency36Choice] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rsn: Optional[MandateSetupReason1Choice] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class CreditorReferenceInformation2:
    tp: Optional[CreditorReferenceType2] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )


@dataclass
class DocumentLineInformation1:
    id: List[DocumentLineIdentification1] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_occurs": 1,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 2048,
        }
    )
    amt: Optional[RemittanceAmount3] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class FinancialInstitutionIdentification18:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        }
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        }
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    pstl_adr: Optional[PostalAddress24] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    othr: Optional[GenericFinancialIdentification1] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class NameAndAddress16:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        }
    )
    adr: Optional[PostalAddress24] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )


@dataclass
class Party38Choice:
    org_id: Optional[OrganisationIdentification29] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    prvt_id: Optional[PersonIdentification13] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class TaxAmount3:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        }
    )
    taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "TaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dtls: List[TaxRecordDetails3] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class BranchAndFinancialInstitutionIdentification6:
    fin_instn_id: Optional[FinancialInstitutionIdentification18] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    brnch_id: Optional[BranchData3] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class Cheque11:
    chq_tp: Optional[ChequeType2Code] = field(
        default=None,
        metadata={
            "name": "ChqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    chq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    chq_fr: Optional[NameAndAddress16] = field(
        default=None,
        metadata={
            "name": "ChqFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dlvry_mtd: Optional[ChequeDeliveryMethod1Choice] = field(
        default=None,
        metadata={
            "name": "DlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dlvr_to: Optional[NameAndAddress16] = field(
        default=None,
        metadata={
            "name": "DlvrTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    chq_mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChqMtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    memo_fld: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MemoFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        }
    )
    rgnl_clr_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnlClrZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    prt_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    sgntr: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        }
    )


@dataclass
class PartyIdentification135:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    pstl_adr: Optional[PostalAddress24] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    id: Optional[Party38Choice] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[A-Z]{2,2}",
        }
    )
    ctct_dtls: Optional[Contact4] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class ReferredDocumentInformation7:
    tp: Optional[ReferredDocumentType4] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    line_dtls: List[DocumentLineInformation1] = field(
        default_factory=list,
        metadata={
            "name": "LineDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class RemittanceLocationData1:
    mtd: Optional[RemittanceLocationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    elctrnc_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 2048,
        }
    )
    pstl_adr: Optional[NameAndAddress16] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class TaxRecord3:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ctgy_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtgyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    dbtr_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    prd: Optional[TaxPeriod3] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    tax_amt: Optional[TaxAmount3] = field(
        default=None,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )


@dataclass
class Garnishment3:
    tp: Optional[GarnishmentType1] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    grnshee: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "Grnshee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    grnshmt_admstr: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "GrnshmtAdmstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    fmly_mdcl_insrnc_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FmlyMdclInsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    mplyee_termntn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MplyeeTermntnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class GroupHeader95:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    authstn: List[Authorisation1Choice] = field(
        default_factory=list,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "max_occurs": 2,
        }
    )
    nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        }
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "total_digits": 18,
            "fraction_digits": 17,
        }
    )
    initg_pty: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    fwdg_agt: Optional[BranchAndFinancialInstitutionIdentification6] = field(
        default=None,
        metadata={
            "name": "FwdgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    initn_src: Optional[PaymentInitiationSource1] = field(
        default=None,
        metadata={
            "name": "InitnSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class RemittanceLocation7:
    rmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    rmt_lctn_dtls: List[RemittanceLocationData1] = field(
        default_factory=list,
        metadata={
            "name": "RmtLctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class TaxData1:
    cdtr: Optional[TaxParty1] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dbtr: Optional[TaxParty2] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ultmt_dbtr: Optional[TaxParty2] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        }
    )
    rcrd: List[TaxRecord3] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class TaxInformation10:
    cdtr: Optional[TaxParty1] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dbtr: Optional[TaxParty2] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmount] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        }
    )
    rcrd: List[TaxRecord3] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class StructuredRemittanceInformation17:
    rfrd_doc_inf: List[ReferredDocumentInformation7] = field(
        default_factory=list,
        metadata={
            "name": "RfrdDocInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rfrd_doc_amt: Optional[RemittanceAmount2] = field(
        default=None,
        metadata={
            "name": "RfrdDocAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdtr_ref_inf: Optional[CreditorReferenceInformation2] = field(
        default=None,
        metadata={
            "name": "CdtrRefInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    invcr: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "Invcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    invcee: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "Invcee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    tax_rmt: Optional[TaxData1] = field(
        default=None,
        metadata={
            "name": "TaxRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    grnshmt_rmt: Optional[Garnishment3] = field(
        default=None,
        metadata={
            "name": "GrnshmtRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    addtl_rmt_inf: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 140,
        }
    )


@dataclass
class RemittanceInformation21:
    ustrd: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    strd: List[StructuredRemittanceInformation17] = field(
        default_factory=list,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class CreditTransferTransaction54:
    pmt_id: Optional[PaymentIdentification6] = field(
        default=None,
        metadata={
            "name": "PmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    pmt_tp_inf: Optional[PaymentTypeInformation26] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    amt: Optional[AmountType4Choice] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    xchg_rate_inf: Optional[ExchangeRate1] = field(
        default=None,
        metadata={
            "name": "XchgRateInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    chrg_br: Optional[ChargeBearerType1Code] = field(
        default=None,
        metadata={
            "name": "ChrgBr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    mndt_rltd_inf: Optional[CreditTransferMandateData1] = field(
        default=None,
        metadata={
            "name": "MndtRltdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    chq_instr: Optional[Cheque11] = field(
        default=None,
        metadata={
            "name": "ChqInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ultmt_dbtr: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification6] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    intrmy_agt1_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification6] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    intrmy_agt2_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification6] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    intrmy_agt3_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification6] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdtr_agt_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdtr: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdtr_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    ultmt_cdtr: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    instr_for_cdtr_agt: List[InstructionForCreditorAgent3] = field(
        default_factory=list,
        metadata={
            "name": "InstrForCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    instr_for_dbtr_agt: Optional[InstructionForDebtorAgent1] = field(
        default=None,
        metadata={
            "name": "InstrForDbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    purp: Optional[Purpose2Choice] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rgltry_rptg: List[RegulatoryReporting3] = field(
        default_factory=list,
        metadata={
            "name": "RgltryRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "max_occurs": 10,
        }
    )
    tax: Optional[TaxInformation10] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    rltd_rmt_inf: List[RemittanceLocation7] = field(
        default_factory=list,
        metadata={
            "name": "RltdRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "max_occurs": 10,
        }
    )
    rmt_inf: Optional[RemittanceInformation21] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    splmtry_data: List[SupplementaryData1] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class PaymentInstruction40:
    pmt_inf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtInfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        }
    )
    pmt_mtd: Optional[PaymentMethod3Code] = field(
        default=None,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    reqd_advc_tp: Optional[AdviceType1] = field(
        default=None,
        metadata={
            "name": "ReqdAdvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    btch_bookg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BtchBookg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "pattern": r"[0-9]{1,15}",
        }
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "total_digits": 18,
            "fraction_digits": 17,
        }
    )
    pmt_tp_inf: Optional[PaymentTypeInformation26] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    reqd_exctn_dt: Optional[DateAndDateTime2Choice] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    poolg_adjstmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PoolgAdjstmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    dbtr: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    dbtr_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification6] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    dbtr_agt_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    instr_for_dbtr_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrForDbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_length": 1,
            "max_length": 140,
        }
    )
    ultmt_dbtr: Optional[PartyIdentification135] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    chrg_br: Optional[ChargeBearerType1Code] = field(
        default=None,
        metadata={
            "name": "ChrgBr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    chrgs_acct: Optional[CashAccount40] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    chrgs_acct_agt: Optional[BranchAndFinancialInstitutionIdentification6] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )
    cdt_trf_tx_inf: List[CreditTransferTransaction54] = field(
        default_factory=list,
        metadata={
            "name": "CdtTrfTxInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_occurs": 1,
        }
    )


@dataclass
class CustomerCreditTransferInitiationV11:
    grp_hdr: Optional[GroupHeader95] = field(
        default=None,
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "required": True,
        }
    )
    pmt_inf: List[PaymentInstruction40] = field(
        default_factory=list,
        metadata={
            "name": "PmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
            "min_occurs": 1,
        }
    )
    splmtry_data: List[SupplementaryData1] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11",
        }
    )


@dataclass
class Document:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:pain.001.001.11"

    cstmr_cdt_trf_initn: Optional[CustomerCreditTransferInitiationV11] = field(
        default=None,
        metadata={
            "name": "CstmrCdtTrfInitn",
            "type": "Element",
            "required": True,
        }
    )
