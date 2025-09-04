from expense import Expense

class Settlement:
    def __init__(self, all_expenses):
        self.expenses: list[Expense] = list(all_expenses)
        self.balanced_ledger: dict[str, dict[str, float]] = {}

    def simplify_ledger(self):
        simplified_ledger: dict[str, dict[str, float]] = {}
        for expense in self.expenses:
            individual_share = expense.amount / len(expense.beneficiaries)
            if expense.payer in simplified_ledger:
                for beneficiary in expense.beneficiaries:
                    if beneficiary == expense.payer:
                        pass
                    elif beneficiary in simplified_ledger[expense.payer]:
                        simplified_ledger[expense.payer][beneficiary] += individual_share
                    else:
                        simplified_ledger[expense.payer].update({beneficiary: individual_share})
            else:
                simplified_ledger.update({expense.payer: {}})
                for beneficiary in expense.beneficiaries:
                    if beneficiary == expense.payer:
                        continue
                    simplified_ledger[expense.payer].update({beneficiary: individual_share})

        return simplified_ledger.copy()

    def settleup(self):
        self.balanced_ledger = self.simplify_ledger()
        delete_debtees: list[str] = []
        for payee, payers in self.balanced_ledger.items():
            delete_debtors: list[tuple[str, str]] = []
            for payer in payers:
                if payer in self.balanced_ledger and payee in self.balanced_ledger[payer]:
                    if self.balanced_ledger[payee][payer] > self.balanced_ledger[payer][payee]:
                        self.balanced_ledger[payee][payer] -= self.balanced_ledger[payer][payee]
                        delete_debtors.append((payer, payee))
                        continue
                    elif self.balanced_ledger[payer][payee] > self.balanced_ledger[payee][payer]:
                        self.balanced_ledger[payer][payee] -= self.balanced_ledger[payee][payer]
                        delete_debtors.append((payee, payer))
                        continue
                    else:
                        delete_debtors.extend([(payee, payer), (payer, payee)])
            for delete_debtor in delete_debtors:
                self.balanced_ledger[delete_debtor[0]].pop(delete_debtor[1])
                if not self.balanced_ledger[delete_debtor[0]]:
                    delete_debtees.append(delete_debtor[0])
        for debtee in delete_debtees:
            self.balanced_ledger.pop(debtee)

        return self.balanced_ledger.copy()
