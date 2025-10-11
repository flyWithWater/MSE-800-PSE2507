


from datetime import datetime
from typing import List, Optional

from sqlalchemy import select

from dao.expense_db import ExpensesDatabase
from entity.expense import ExpenseItem


class ExpenseDAO:
    """Data access helpers that wrap CRUD operations for `ExpenseItem` records."""

    @staticmethod
    def create_expense(
        expense_name: str,
        amount: int,
        create_time: Optional[datetime] = None,
    ) -> ExpenseItem:
        """Insert a new expense and return the persisted entity."""
        with ExpensesDatabase.session_scope() as session:
            expense = ExpenseItem(
                expense_name=expense_name,
                amount=amount,
            )
            if create_time is not None:
                expense.create_time = create_time

            session.add(expense)
            session.flush()
            session.refresh(expense)
            return expense

    @staticmethod
    def get_expense(expense_id: int) -> Optional[ExpenseItem]:
        """Return a single expense by primary key or `None` if missing."""
        with ExpensesDatabase.session_scope(commit=False) as session:
            return session.get(ExpenseItem, expense_id)

    @staticmethod
    def list_expenses(order_by=None) -> List[ExpenseItem]:
        """Return all expenses, optionally ordered by a SQLAlchemy column/expression."""
        statement = select(ExpenseItem)
        if order_by is not None:
            statement = statement.order_by(order_by)

        with ExpensesDatabase.session_scope(commit=False) as session:
            result = session.execute(statement)
            return list(result.scalars().all())

    @staticmethod
    def update_expense(expense_id: int, **updates) -> Optional[ExpenseItem]:
        """Apply field updates to an expense; returns the updated entity or `None`."""
        if not updates:
            return ExpenseDAO.get_expense(expense_id)

        allowed_fields = {"amount", "expense_name", "create_time"}

        with ExpensesDatabase.session_scope() as session:
            expense = session.get(ExpenseItem, expense_id)
            if expense is None:
                return None

            for field, value in updates.items():
                if field not in allowed_fields:
                    continue
                setattr(expense, field, value)

            session.flush()
            session.refresh(expense)
            return expense

    @staticmethod
    def delete_expense(expense_id: int) -> bool:
        """Delete an expense row; returns `True` when a record was removed."""
        with ExpensesDatabase.session_scope() as session:
            expense = session.get(ExpenseItem, expense_id)
            if expense is None:
                return False

            session.delete(expense)
            return True
