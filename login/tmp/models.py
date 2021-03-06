# -*- coding: utf-8 -*-
import schematics.models
from schematics.types import (
    StringType, BooleanType, IntType, FloatType, LongType,
    ListType, ModelType
)


class ErrorResponse(Exception):

    def __init__(self, error=None, errorcode=None, errormessage=None,
                 errordetails=None):
        self.error = error
        self.errorcode = errorcode
        self.errormessage = errormessage
        self.errordetails = errordetails

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return (
            "ErrorResponse(error={}, errorcode={}, errormessage={}"
            ", errordetails={})"
        ).format(self.error, self.errorcode, self.errormessage,
                 self.errordetails)


class Model(schematics.models.Model):

    def __str__(self):
        return repr(self)

    def __repr__(self):
        __ = ", ".join(["{}={}".format(k,v) for k, v in self._data.items()])
        return "{}({})".format(self.__class__.__name__,__)


####################
# Response Models
####################


class AdditionalItemResponse(Model):
    dateline = LongType()
    discount = FloatType()
    discounted_price = LongType()
    item_price = LongType()
    last_post = LongType()
    post_title = StringType()
    thread_id = StringType()
    thread_title = StringType()
    thread_type = IntType()
    thumbnail = StringType()


class MapLocationResponse(Model):
    latitude = FloatType()
    longitude = FloatType()
    name = StringType()


class AddressResponse(Model):
    address = StringType()
    address_id = StringType(deserialize_from=["id", "address_id"])
    area_id = StringType()
    city_id = StringType()
    default = BooleanType()
    map_location = ModelType(MapLocationResponse)
    name = StringType()
    owner_name = StringType()
    owner_phone = StringType()
    province_id = StringType()


class CategoryPermission(Model):
    can_not_view_category = ListType(StringType)
    can_not_view_thread = ListType(StringType)
    can_not_create_thread = ListType(StringType)
    can_not_reply_thread = ListType(StringType)


class ContentResponse(Model):
    description = StringType()
    height = IntType()
    pagetext = StringType()
    thumbnail = StringType(deserialize_from=["thumbnail", "thumbnail_url"])
    thumbnail_compact = StringType()
    url = StringType()
    width = IntType()


class DbUpdateResponse(Model):

    class DbUpdate(Model):
        last_update = LongType()
        type = StringType()

    data = ListType(ModelType(DbUpdate))


class ExtraAttributesResponse(Model):
    attribute = StringType()
    value = StringType()


class ForumResponse(Model):
    description = StringType()
    forum_icon = StringType()
    forum_id = StringType()
    is_subscribed = BooleanType()
    last_post = StringType()
    last_post_id = StringType()
    last_poster = StringType()
    last_thread_id = StringType()
    last_thread_starter = StringType()
    last_thread_title = StringType()
    name = StringType()
    order = StringType()
    post_count = StringType()
    service = StringType()
    sort = StringType()
    thread_count = StringType()
    visible = StringType()


class LocationResponse(Model):

    class Location(Model):
        id = StringType()
        name = StringType()

    class Meta(Model):
        last_update = LongType()

    data = ListType(ModelType(Location))
    meta = ModelType(Meta)


class HotThreadResponse(Model):
    display_name = StringType()
    first_post_id = StringType()
    forum_id = StringType()
    forum_name = StringType()
    hot_thread_start_timestamp = LongType()
    image = StringType()
    image_compact = StringType()
    is_subscribed = BooleanType()
    last_post_id = StringType()
    rating = FloatType()
    reply_count = LongType()
    shared_count = LongType()
    short_url = StringType()
    thread_id = StringType()
    thread_type = IntType()
    title = StringType()
    user_id = StringType()
    username = StringType()
    views = LongType()
    vote_num = LongType()
    vote_total = LongType()


class PaginationResponse(Model):
    current_page = IntType()
    per_page = IntType()
    total = LongType()
    total_current = IntType(deserialize_from=["total_current", "count"])
    total_page = IntType(deserialize_from=["total_page", "total_pages"])


class PairIdLabelResponse(Model):
    id = StringType()
    label = StringType()


class PairIdImageResponse(PairIdLabelResponse):
    image_url = StringType()


class PairIdNameResponse(Model):
    name = StringType(deserialize_from=["name", "value"])


class PollQuestionResponse(Model):
    decoded = StringType()


class PollResponse(Model):
    can_vote = IntType()
    is_open = IntType()
    is_voted = IntType()
    question = ModelType(PollQuestionResponse)
    time_remaining = StringType()
    total_votes = IntType()


class PostResponse(Model):
    dateline = LongType()
    decoded = StringType()
    display_name = StringType()
    enable_reputation = IntType()
    is_donatur = BooleanType()
    is_vsl = BooleanType()
    pagetext = StringType()
    pagetext_noquote = StringType()
    post_id = StringType()
    post_userid = StringType()
    post_username = StringType()
    profilepicture = StringType()
    reputation_box = IntType()
    text = StringType()
    title = StringType()
    usertitle = StringType()


class ResourcesResponse(Model):
    images = ListType(StringType)
    images_thumbnail = ListType(StringType)
    thumbnail = StringType()


class SimpleFeedbackResponse(Model):
    negative = IntType()
    neutral = IntType()
    percentage = IntType()
    point = IntType()
    positive = IntType()


class SectionItemResponse(Model):
    section_item_type = StringType()


class ThreadResponse(SectionItemResponse):

    class ShippingResponse(Model):
        custom_methods = ListType(StringType)
        location = ModelType(AddressResponse)
        methods = ListType(StringType)
        shipping_types = ListType(ModelType(PairIdNameResponse))
        weight = LongType()

    can_buynow = IntType()
    can_nego = IntType()
    content = ModelType(ContentResponse)
    creator = BooleanType()
    dateline = LongType()
    description = StringType()
    discount = FloatType()
    discounted_price = LongType()
    display_name = StringType()
    enable_reputation = IntType()
    extra_attributes = ListType(ModelType(ExtraAttributesResponse))
    feedback = ModelType(SimpleFeedbackResponse)
    first_post_id = StringType()
    first_post_preview = StringType()
    forum_id = StringType()
    forum_name = StringType()
    forum_title = StringType()
    free_shipping = IntType()
    hot_thread = IntType()
    ht_title = StringType()
    initial_prefix_id = StringType()
    is_donatur = BooleanType()
    is_instant_purchase = BooleanType()
    is_offered = BooleanType()
    is_rated = BooleanType()
    is_seller_inactive = BooleanType()
    is_subscribed = BooleanType()
    is_vsl = BooleanType()
    item_condition = StringType()
    item_location = StringType()
    item_price = LongType()
    joindate = LongType()
    last_post = LongType()
    last_post_id = StringType()
    last_post_userid = StringType()
    last_poster = StringType()
    meta_images = ListType(StringType)
    number_of_post = StringType()
    open = IntType()
    parent_list = StringType()
    payment_mechanism = ListType(StringType)
    poll = ModelType(PollResponse)
    poll_id = IntType()
    post_id = StringType()
    post_title = StringType()
    post_userid = StringType()
    post_username = StringType()
    prefix_id = StringType()
    profilepicture = StringType()
    reply_count = LongType()
    reputation = IntType()
    reputation_box = IntType()
    reputation_title = StringType()
    resources = ModelType(ResourcesResponse)
    seller_reputation = ModelType(PairIdImageResponse)
    shared_count = LongType()
    shipping = ModelType(ShippingResponse)
    short_url = StringType()
    sold_count = IntType()
    sticky = IntType()
    sundul_count = IntType()
    sundul_count_remainder = IntType()
    sundul_enabled = IntType()
    tagsearch = StringType()
    thread_id = StringType()
    thread_starter = StringType()
    thread_type = IntType()
    thumbnail_compact = StringType()
    title = StringType()
    url = StringType()
    usergroupid = StringType()
    usertitle = StringType()
    views = LongType()
    visible = IntType()
    vote_num = LongType()
    vote_total = LongType()


class HighlightResponse(ThreadResponse):
    image = StringType()
    link = StringType()
    section = StringType()


class ForumListResponse(Model):

    class JbSettingsResponse(Model):
        max_price = LongType()
        min_price = LongType()
        product_type = IntType()

    child_list = StringType()
    description = StringType()
    display_order = StringType()
    forum_id = StringType()
    icon_url = StringType()
    jb_settings = ModelType(JbSettingsResponse)
    name = StringType()
    parent_id = StringType()
    parent_list = StringType()
    redirect_forum_id = StringType()
    redirect_forum_type = StringType()
    type_list = StringType()
    visible = StringType()


class ForumStreamResponse(Model):

    class Meta(Model):
        cursor = StringType()

    data = ListType(ModelType(ThreadResponse))
    meta = ModelType(Meta)


class MultipleHotThreadResponse(Model):

    class Meta(Model):
        cached = BooleanType()
        cached_from = LongType()

    data = ListType(ModelType(HotThreadResponse))
    meta = ModelType(Meta)


class MultipleThreadListResponse(PaginationResponse):
    forum = ModelType(ForumResponse)
    subforum = ListType(ModelType(ForumResponse))
    tags = ListType(StringType)
    thread = ListType(ModelType(ThreadResponse))
    thread_num = LongType()
    top_feature = ListType(ModelType(HighlightResponse))
    top_thread = ListType(ModelType(ThreadResponse))
    total_thread = LongType()


class MultipleThreadResponse(PaginationResponse):
    more_from_seller = ListType(ModelType(AdditionalItemResponse))
    posts = ListType(ModelType(PostResponse))
    similar = ListType(ModelType(AdditionalItemResponse))
    thread = ModelType(ThreadResponse)
    total_post = LongType()


class SearchMetaResponse(PaginationResponse):
    numFound = LongType()


class SearchThreadResponse(SearchMetaResponse):
    cursor = StringType()
    item = ListType(ModelType(ThreadResponse))
    querytime = FloatType()
    start = IntType()


class SmileyResponse(Model):
    text = StringType()
    url = StringType()


class SpecialEventResponse(Model):
    end_date = LongType()
    id = StringType()
    image_path = StringType()
    start_date = LongType()
    url = StringType()


class MultipleSpecialEventResponse(Model):
    data = ListType(ModelType(SpecialEventResponse))


class TopVideoResponse(Model):

    class TopVideo(ThreadResponse):
        thumbnail = StringType()
        thumbnail_compact = StringType()

    data = ListType(ModelType(TopVideo))


class VersionResponse(Model):
    latest_version = StringType()
    required = BooleanType()
    update = BooleanType()
