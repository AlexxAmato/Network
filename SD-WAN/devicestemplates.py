import requests
import json
import click
import tabulate




@click.group()
def cli():
    """Command line tool for deploying templates to CISCO SDWAN.
    """
    pass

@click.command()
def device_list():
    click.secho('retrieving the devices')
    url = base_url + "/device"
    response = requests.get(url=url,headers=headers,verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print('failed to get device list')
        exit()
    
    headers = ['host-name', 'device-type', 'device-id', 'system-ip', 'site-ID']
    table = list()


    for item in items:
        tr = [item['host-name'], item['device-type'], item['Uuid']]
        table.append(tr)
    try:
        click.echo(tablulate.tabulate(table,headers,tablefmt='fancy-grid'))
    except UnicodeEncodeError:
        click.echo(tabulate.tablulate(table, headres, tablefmt=grid))



@click.command()
def template_list():
    url = base_url + '/template/device'
    response = requests.get(url=url, headres=headers, verify=False)
    if response.status_code == 200:
        ietms = response.json()['data']
    else:
        print('failed to get list of templates')

    headers = ['template-name', 'device-type', 'template-id', 'attached-devices']
    table = list()

    for item in items:
        tr = [item['templateName'], item['deviceType'], item['templateId'], item['devicesAttached']]
        table.append(tr)
    try:
        click.echo(tabulate.tabulate)


@click.command()
@click.option()
def attached_devices():
    url= 'dataservice/template/device/config/attached{0}'.format(template)

    response = request.get(url=url, heares=headers, verify=False)
    items = response.json()['data']


    headers = ['host name', 'device IP', "site id", 'host type']
    table = list()


@click.command()
#endpoint that the call will be made to is 
#https://{{vmanage}}:{{port}}/dataservice/template/device/config/attachfeature
def attach(template, variables):
    with open(variables) as f:
        config = yaml.safe_load(f.read())

system_ip = config.get('system_ip')
host_name = config.get('host_name')
template_id = template

template_variables = {
    cvs-status: 'complete',
    'cvs-deviceid': config.get("device_id")

}

@click.command()
def detach():
    pass

cli.add_command(attach)
cli.add_command(detach)
cli.add_command(device_list)
cli.add_command(attached_devices)
cli.add_command(template_list)

if __name__ == "__main__":
    cli()


Mandatory_payload for attaching config:
    
    {
  "deviceTemplateList":[
  {
    "templateId":"41f6a440-c5cc-4cc6-9ca1-af18e332a781",
    "device":[
    {
      "csv-status":"complete",
      "csv-deviceId":"5e5f45e7-3062-44b2-b6f6-40c682149e05",
      "csv-deviceIP":"172.16.255.11",
      "csv-host-name":"vm1",
      "//system/host-name":"vm1",
      "//system/system-ip":"172.16.255.11",
      "//system/site-id":"100",
      "csv-templateId":"41f6a440-c5cc-4cc6-9ca1-af18e332a781",
      "selected":"true"
    }
    ],
    "isEdited":false,
    "isMasterEdited":false
  }
  ]
}