"""
Django admin declarations
"""

from django.contrib import admin
from django.utils.safestring import mark_safe

from aa_forum.models import Board, Category, Topic


class BaseReadOnlyAdminMixin:
    """
    Base "Read Only" mixin for admin models
    """

    def has_add_permission(self, request):
        """
        Has add permissions
        :param request:
        :type request:
        :return:
        :rtype:
        """

        return False

    def has_change_permission(self, request, obj=None):
        """
        Has change permissions
        :param request:
        :type request:
        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        return False

    def has_delete_permission(self, request, obj=None):
        """
        Has delete permissions
        :param request:
        :type request:
        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        return False


@admin.register(Category)
class CategoryAdmin(BaseReadOnlyAdminMixin, admin.ModelAdmin):
    """
    Category admin
    """

    list_display = ("name", "slug", "_board_count")
    exclude = ("is_collapsible",)

    def _board_count(self, obj):
        """
        Return the board count per category
        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        return obj.boards.count()


@admin.register(Board)
class BoardAdmin(BaseReadOnlyAdminMixin, admin.ModelAdmin):
    """
    Board admin
    """

    list_display = (
        "name",
        "slug",
        "parent_board",
        "_groups",
        "category",
        "_topics_count",
    )

    def _groups(self, obj):
        """
        Return the groups this board is restricted to as list
        :return:
        :rtype:
        """

        groups = obj.groups.all()

        if groups.count() > 0:
            return mark_safe("<br>".join([group.name for group in groups]))

        return ""

    def _topics_count(self, obj):
        """
        Return the topics count per board
        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        return obj.topics.count()


@admin.register(Topic)
class TopicAdmin(BaseReadOnlyAdminMixin, admin.ModelAdmin):
    """
    Topic admin
    """

    list_display = ("subject", "slug", "board", "_messages_count")

    def _messages_count(self, obj):
        """
        Return the message count per topic
        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        return obj.messages.count()
