from typing import Annotated
from datetime import datetime

from pydantic import BaseModel, Field

OptStr = Annotated[str | None, Field(default=None)]
OptInt = Annotated[int | None, Field(default=None)]
OptFloat = Annotated[float | None, Field(default=None)]
OptBool = Annotated[bool | None, Field(default=None)]


class ObjectsResponse(BaseModel):
    total: int
    objectIDs: list[int] | None = None


class Constituent(BaseModel):
    constituentID: int = Field(ge=1)
    role: OptStr
    name: OptStr
    constituentULAN_URL: OptStr
    constituentWikidata_URL: OptStr
    gender: OptStr


class DimensionParsed(BaseModel):
    element: OptStr
    dimensionType: OptStr
    dimension: OptFloat


class Measurements(BaseModel):
    Height: OptFloat
    Length: OptFloat
    Width: OptFloat


class Element(BaseModel):
    elementName: OptStr
    elementDescription: OptStr
    elementMeasurements: Measurements | None = None


class Tag(BaseModel):
    term: OptStr
    AAT_URL: OptStr
    Wikidata_URL: OptStr


class ObjectResponse(BaseModel):
    objectID: int = Field(ge=1)
    isHighlight: OptBool
    accessionNumber: OptStr
    accessionYear: OptStr
    isPublicDomain: OptBool
    primaryImage: OptStr
    primaryImageSmall: OptStr
    additionalImages: list[str] | None = None
    constituents: list[Constituent] | None = None
    department: OptStr
    objectName: OptStr
    title: OptStr
    culture: OptStr
    period: OptStr
    dynasty: OptStr
    reign: OptStr
    portfolio: OptStr
    artistRole: OptStr
    artistPrefix: OptStr
    artistDisplayName: OptStr
    artistDisplayBio: OptStr
    artistSuffix: OptStr
    artistAlphaSort: OptStr
    artistNationality: OptStr
    artistBeginDate: OptStr
    artistEndDate: OptStr
    artistGender: OptStr
    artistWikidata_URL: OptStr
    artistULAN_URL: OptStr
    objectDate: OptStr
    objectBeginDate: OptInt
    objectEndDate: OptInt
    medium: OptStr
    dimensions: OptStr
    dimensionsParsed: list[DimensionParsed] | None = None
    measurements: list[Element] | None = None
    creditLine: OptStr
    geographyType: OptStr
    city: OptStr
    state: OptStr
    county: OptStr
    country: OptStr
    region: OptStr
    subregion: OptStr
    locale: OptStr
    locus: OptStr
    excavation: OptStr
    river: OptStr
    classification: OptStr
    rightsAndReproduction: OptStr
    linkResource: OptStr
    metadataDate: datetime | None = None
    repository: OptStr
    objectURL: OptStr
    tags: list[Tag] | None = None
    objectWikidata_URL: OptStr
    isTimelineWork: OptBool
    GalleryNumber: OptStr


class Department(BaseModel):
    departmentId: int = Field(ge=1)
    displayName: OptStr


class DepartmentsResponse(BaseModel):
    departments: list[Department] | None = None
