from typing import Optional

from robotlibcore import keyword

from OpenShiftCLI.base import LibraryComponent
from OpenShiftCLI.cliclient import CliClient
from OpenShiftCLI.dataloader import DataLoader
from OpenShiftCLI.dataparser import DataParser
from OpenShiftCLI.outputformatter import OutputFormatter
from OpenShiftCLI.outputstreamer import OutputStreamer


class NetworkpolicyKeywords(LibraryComponent):
    def __init__(self,
                 cli_client: CliClient,
                 data_loader: DataLoader,
                 data_parser: DataParser,
                 output_formatter: OutputFormatter,
                 output_streamer: OutputStreamer) -> None:
        LibraryComponent.__init__(self, cli_client, data_loader, data_parser, output_formatter, output_streamer)

    @keyword
    def apply_network_policy(self, file: str, namespace: Optional[str] = None) -> None:
        """Apply Network Policy

        Args:
            file (str): Path to the yaml file containing the Network Policy definition
            namespace (Optional[str], optional): Namespace where the Network Policy exists. Defaults to None.
        """
        self.process(operation="apply", type="body", data_type="yaml", file=file, namespace=namespace)

    @keyword
    def create_network_policy(self, file: str, namespace: Optional[str] = None) -> None:
        """Create Network Policy

        Args:
            file (str): Path to the yaml file containing the Network Policy definition
            namespace (Optional[str], optional): Namespace where the Network Policy will be created
        """
        self.process(operation="create", type="body", data_type="yaml", file=file, namespace=namespace)

    @keyword
    def delete_network_policy(self, name: str, namespace: Optional[str] = None, **kwargs: str) -> None:
        """Delete Network Policy

        Args:
            name (str):  Network Policy to delete
            namespace (Optional[str], optional): Namespace where the Network Policy exists. Defaults to None.
        """
        self.process(operation="delete", type="name", name=name, namespace=namespace, **kwargs)
