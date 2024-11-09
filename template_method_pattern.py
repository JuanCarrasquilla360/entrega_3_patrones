from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

class ReportTemplate(ABC):
    def generate_report(self) -> str:
        """Template method que define el esqueleto del algoritmo."""
        data = self.collect_data()
        processed_data = self.process_data(data)
        if self.validate_data(processed_data):
            return self.export_report(processed_data)
        return "Error: Datos no válidos para el reporte"
    
    @abstractmethod
    def collect_data(self) -> List[Dict]:
        """Recolecta los datos necesarios para el reporte."""
        pass
    
    @abstractmethod
    def process_data(self, data: List[Dict]) -> List[Dict]:
        """Procesa los datos recolectados."""
        pass
    
    @abstractmethod
    def validate_data(self, data: List[Dict]) -> bool:
        """Valida los datos procesados."""
        pass
    
    @abstractmethod
    def export_report(self, data: List[Dict]) -> str:
        """Exporta los datos en el formato requerido."""
        pass

class SalesReport(ReportTemplate):
    def collect_data(self) -> List[Dict]:
    
        return [
            {"id": 1, "product": "Laptop", "amount": 1200, "date": "2024-01-01"},
            {"id": 2, "product": "Mouse", "amount": 25, "date": "2024-01-01"}
        ]
    
    def process_data(self, data: List[Dict]) -> List[Dict]:
    
        total_sales = sum(item["amount"] for item in data)
        processed_data = data.copy()
        for item in processed_data:
            item["processed_date"] = datetime.now().strftime("%Y-%m-%d")
        processed_data.append({"total_sales": total_sales})
        return processed_data
    
    def validate_data(self, data: List[Dict]) -> bool:
    
        return all(item.get("amount", 0) > 0 for item in data if "amount" in item)
    
    def export_report(self, data: List[Dict]) -> str:
    
        return f"Reporte de Ventas generado con {len(data)-1} transacciones. Total: ${data[-1]['total_sales']}"

class InventoryReport(ReportTemplate):
    def collect_data(self) -> List[Dict]:
    
        return [
            {"id": 1, "product": "Laptop", "stock": 50, "min_stock": 10},
            {"id": 2, "product": "Mouse", "stock": 100, "min_stock": 20}
        ]
    
    def process_data(self, data: List[Dict]) -> List[Dict]:
    
        processed_data = data.copy()
        for item in processed_data:
            item["status"] = "OK" if item["stock"] > item["min_stock"] else "REORDER"
        return processed_data
    
    def validate_data(self, data: List[Dict]) -> bool:
    
        return all(item.get("stock", 0) >= 0 for item in data)
    
    def export_report(self, data: List[Dict]) -> str:
    
        reorder_items = sum(1 for item in data if item["status"] == "REORDER")
        return f"Reporte de Inventario generado con {len(data)} productos. Productos a reordenar: {reorder_items}"

class HRReport(ReportTemplate):
    def collect_data(self) -> List[Dict]:
    
        return [
            {"id": 1, "name": "John Doe", "department": "IT", "hours_worked": 160},
            {"id": 2, "name": "Jane Smith", "department": "HR", "hours_worked": 152}
        ]
    
    def process_data(self, data: List[Dict]) -> List[Dict]:
    
        processed_data = data.copy()
        for item in processed_data:
            item["overtime"] = max(0, item["hours_worked"] - 150)
        return processed_data
    
    def validate_data(self, data: List[Dict]) -> bool:
    
        return all(0 <= item.get("hours_worked", 0) <= 200 for item in data)
    
    def export_report(self, data: List[Dict]) -> str:
    
        total_overtime = sum(item["overtime"] for item in data)
        return f"Reporte de RRHH generado con {len(data)} empleados. Total horas extra: {total_overtime}"

def main():

    sales_report = SalesReport()
    inventory_report = InventoryReport()
    hr_report = HRReport()
    

    print("Generando reportes:")
    print(sales_report.generate_report())
    print(inventory_report.generate_report())
    print(hr_report.generate_report())

if __name__ == "__main__":
    main()