# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_confidentialledger_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_confidentialledger.vendored_sdks.confidentialledger import ConfidentialLedger
    return get_mgmt_service_client(cli_ctx,
                                   ConfidentialLedger)


def cf_ledger(cli_ctx, *_):
    return cf_confidentialledger_cl(cli_ctx).ledger