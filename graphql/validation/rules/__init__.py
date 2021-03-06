"""graphql.validation.rules package"""

from typing import Type

from ...error import GraphQLError
from ...language.visitor import Visitor
from ..validation_context import (
    ASTValidationContext,
    SDLValidationContext,
    ValidationContext,
)

__all__ = ["ASTValidationRule", "SDLValidationRule", "ValidationRule", "RuleType"]


class ASTValidationRule(Visitor):

    context: ASTValidationContext

    def __init__(self, context: ASTValidationContext) -> None:
        self.context = context

    def report_error(self, error: GraphQLError):
        self.context.report_error(error)


class SDLValidationRule(ASTValidationRule):

    context: ValidationContext

    def __init__(self, context: SDLValidationContext) -> None:
        super().__init__(context)


class ValidationRule(ASTValidationRule):

    context: ValidationContext

    def __init__(self, context: ValidationContext) -> None:
        super().__init__(context)


RuleType = Type[ASTValidationRule]
