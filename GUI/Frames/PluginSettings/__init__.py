from .Auth0 import Auth0
from .Base64 import Base64
from .Blurhash import Blurhash
from .Cloudinary import Cloudinary
from .CloudStorage import CloudStorage
from .DefaultRoles import DefaultRoles
from .FormBuilder import FormBuilder
from .GoogleOneTap import GoogleOneTap
from .HashUpload import HashUpload
from .ImageKit import ImageKit
from .Lexical import Lexical
from .NestedDocs import NestedDocs
from .oAuth import oAuth
from .PasswordProtection import PasswordProtection
from .PhoneField import PhoneField
from .Redirects import Redirects
from .RedisCache import RedisCache
from .ResolveAlias import ResolveAlias
from .S3Upload import S3Upload
from .Search import Search
from .SEO import SEO
from .Stripe import Stripe
from .Tenency import Tenency
from .webP import webP
from .Zapier import Zapier

class PluginSettings():
  def __init__(self):
    self.Auth0 = Auth0
    self.Base64 = Base64
    self.Blurhash = Blurhash
    self.Cloudinary = Cloudinary
    self.CloudStorage = CloudStorage
    self.DefaultRoles = DefaultRoles
    self.FormBuilder = FormBuilder
    self.GoogleOneTap = GoogleOneTap
    self.HashUpload = HashUpload
    self.ImageKit = ImageKit
    self.Lexical = Lexical
    self.NestedDocs = NestedDocs
    self.oAuth = oAuth
    self.PasswordProtection = PasswordProtection
    self.PhoneField = PhoneField
    self.Redirects = Redirects
    self.RedisCache = RedisCache
    self.ResolveAlias = ResolveAlias
    self.S3Upload = S3Upload
    self.Search = Search
    self.SEO = SEO
    self.Stripe = Stripe
    self.Tenency = Tenency
    self.webP = webP
    self.Zapier = Zapier