from typing import Any

from pydantic import BaseModel

from test_framework.schemas.enums import AssertMode


class BaseAsserts:
    def assert_models(
        self,
        expected_model: BaseModel,
        actual_model: BaseModel,
        assert_mode: AssertMode,
    ):
        """
        Сравнивает две модели Pydantic на основе заданного режима проверки.

        :param expected_model: Ожидаемая модель.
        :param actual_model: Фактическая модель.
        :param assert_mode: Режим проверки: SOFT - ожидаемая модель полностью входит в фактическую или FULL - модели полностью совпадают.
        :raises AssertionError: Если модели не совпадают согласно режиму проверки.
        """
        expected_dict = expected_model.model_dump(exclude_unset=True)
        actual_dict = actual_model.model_dump(exclude_unset=True)

        match assert_mode:
            case AssertMode.SOFT:
                self._compare_dicts(expected_dict, actual_dict)
            case AssertMode.FULL:
                assert (
                    expected_dict == actual_dict
                ), f"Модели не совпадают. Ожидается: {expected_dict}, фактическая: {actual_dict}"

    @staticmethod
    def _compare_values(expected_value: Any, actual_value: Any, path: str):
        assert (
            actual_value == expected_value
        ), f"Поле '{path}' имеет значение {actual_value}, ожидается {expected_value}"

    def _compare_dicts(self, expected: dict, actual: dict, path: str = ""):
        for field, expected_value in expected.items():
            assert (
                field in actual
            ), f"Поле '{path + field}' не найдено в фактической модели"
            actual_value = actual[field]
            if isinstance(expected_value, dict) and isinstance(actual_value, dict):
                self._compare_dicts(expected_value, actual_value, path + field + ".")
            else:
                self._compare_values(expected_value, actual_value, path + field)
