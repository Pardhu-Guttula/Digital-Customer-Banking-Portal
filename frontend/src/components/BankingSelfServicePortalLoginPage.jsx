import React from "react";
import { useIntl } from "react-intl";
import PageBackgroundCanvas from "./layout/PageBackgroundCanvas";
import CenteredAuthStackWrapper from "./BankingSelfServicePortalLoginPage/CenteredAuthStackWrapper";

export default function BankingSelfServicePortalLoginPage() {
  const intl = useIntl();

  return (
    <main
      aria-label={intl.formatMessage({
        id: "bankingSelfServicePortalLoginPage.mainAriaLabel",
      })}
    >
      <PageBackgroundCanvas>
        <CenteredAuthStackWrapper />
      </PageBackgroundCanvas>
    </main>
  );
}