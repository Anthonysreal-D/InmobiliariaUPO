/** @odoo-module **/

import { useDispatch, useState } from '@web/core/utils/hooks';
import { registry } from '@web/core/registry';

const { Component } = owl;

class C2Componente extends Component {
    constructor() {
        super(...arguments);
        this.dispatch = useDispatch();
    }

    async willStart() {
        this.state.subastas = await this.rpc({
            model: 'inmobiliaria_upo.subasta',
            method: 'search_read',
            args: [[]],
            kwargs: { fields: ['name', 'valorInicial'] },
        });
    }

    setup() {
        this.state = useState({
            subastas: [],
        });

        this.dispatch("loadSubastas");
    }
}

C2Componente.template = 'owl.C2Componente';
registry.category('actions').add('owl.action_C2Componente_js', C2Componente);


